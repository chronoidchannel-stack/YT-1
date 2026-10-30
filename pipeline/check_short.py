"""Validate storyboard and normalize approved scene images (no drawing/overlays)."""
import argparse
import re
from pathlib import Path


def scenes(path):
    text = Path(path).read_text(encoding='utf-8')
    blocks = re.split(r'^### Adegan ', text, flags=re.M)[1:]
    result = []
    for block in blocks:
        number, chunk = re.match(r'(\d+) \| c(\d+)', block).groups()
        vo = re.search(r'^- \*\*VO:\*\* (.+)$', block, re.M).group(1)
        name = re.search(r'^- \*\*File:\*\* `([^`]+)`', block, re.M).group(1)
        result.append((int(number), int(chunk), vo, name))
    return result


def validate(items):
    errors = []
    if [x[0] for x in items] != list(range(1, 31)):
        errors.append('Expected scenes 01–30 in order')
    if len({x[3] for x in items}) != len(items):
        errors.append('Duplicate image filenames')
    for number, chunk, vo, name in items:
        if chunk != (number - 1) // 5 + 1:
            errors.append(f'Scene {number}: incorrect VO chunk')
        if not 12 <= len(vo.split()) <= 13:
            errors.append(f'Scene {number}: expected 12–13 words, got {len(vo.split())}')
        if Path(name).name != name or not name.endswith('.jpg'):
            errors.append(f'Scene {number}: invalid filename')
    return errors


def normalize(source, destination):
    from PIL import Image, ImageOps, ImageFilter
    if source.resolve() == destination.resolve():
        raise ValueError('Keep raw images: output must be a different path')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image).convert('RGB')
        image = ImageOps.fit(image, (1080, 1920), method=Image.Resampling.LANCZOS)
        image = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=115, threshold=2))
        image.save(destination, 'JPEG', quality=96, subsampling=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('script', type=Path)
    parser.add_argument('--images', type=Path, default=Path('assets/images'))
    parser.add_argument('--normalize-to', type=Path, help='Only after manual visual approval')
    args = parser.parse_args()
    items = scenes(args.script)
    errors = validate(items)
    for error in errors:
        print('ERROR:', error)
    if errors:
        raise SystemExit(1)
    print(f'PASS: {len(items)} scenes, {sum(len(x[2].split()) for x in items)} words, 6 chunks')
    present = 0
    for number, _, _, name in items:
        source = args.images / name
        if source.exists():
            present += 1
            if args.normalize_to:
                normalize(source, args.normalize_to / name)
        else:
            print(f'MISSING scene {number:02}: {name}')
    print(f'Images available: {present}/30. Availability is NOT visual approval.')


if __name__ == '__main__':
    main()

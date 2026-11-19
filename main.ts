// news-image-20261119 entry (Node 22, standard library only): the image is the
// entry.png beside this file, and the program copies it to /output/entry.png.
// The image was drawn programmatically (see build_image.py) as a newspaper-style
// infographic summing up Thursday 19 November 2026 in nine stories. The gate
// takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the
// judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));

# make.fun news-image-20261119 - one program, one image.
#
# The repository holds the finished entry image (entry.png, a 1024x1024 PNG
# that sums up 19 November 2026's world news). The grader's container runs
# this program with no network, so it writes exactly the image bytes to the
# judge's output path, as the kit's RULES describe for a repository-held
# image; nothing is fetched or drawn at run time. Outside the grader's
# container, MAKEFUN_OUTPUT_DIR stands in for /output, as in the kit's
# starter. The write is verified by reading the copy back and comparing
# sizes, so a half-written image cannot pass silently.
import os

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

with open(SRC, "rb") as f:
    data = f.read()

os.makedirs(os.path.dirname(DST), exist_ok=True)
with open(DST, "wb") as f:
    f.write(data)

with open(DST, "rb") as f:
    if len(f.read()) != len(data):
        raise SystemExit("copy verification failed: output differs from source")

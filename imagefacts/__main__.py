import sys

import imagefacts


def main(args):
    for arg in args:
        print repr(imagefacts.facts(arg))
    return 0


sys.exit(main(sys.argv[1:]))

import sys
import os

def run():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.join(base, 'mail'))
    sys.path.insert(0, os.path.join(base, 'python-modargs'))
    sys.path.insert(0, os.path.join(base, 'lamson'))
    sys.path.insert(0, os.path.join(base, 'mail'))

    from modargs import args
    from lamson import commands

    args.parse_and_run_command(sys.argv[1:], commands, default_command="help")


if __name__ == '__main__':
    exit = run()
    if exit:
        sys.exit(exit)

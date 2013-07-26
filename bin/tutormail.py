import sys
import os

# mftutor@pulerau:~/mail$ PYTHONPATH=/home/mftutor/deps/pymodules ../deps/lamson-git/bin/lamson start -chdir /home/mftutor/mail -debug -pid /home/mftutor/mail/run/smtp.pid

def run():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(os.path.join(base, 'mail'))
    sys.path.insert(0, os.path.join(base, 'python-modargs'))
    sys.path.insert(0, os.path.join(base, 'lamson'))
    sys.path.insert(0, os.path.join(base, 'mail'))
    import lamson.commands
    return lamson.commands.start_command(debug=True)


if __name__ == '__main__':
    exit = run()
    if exit:
        sys.exit(exit)

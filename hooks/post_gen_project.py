import subprocess
import os


def install_requirements():
    subprocess.call(['pip', 'install', '-r', 'requirements/local.txt'])


def setup_database():
    curdir_name = os.getcwd().split(os.sep)[-1]
    sql_cmd = 'create database {0};'.format(curdir_name)
    subprocess.call(['mysql', '-u', 'root', '-e', sql_cmd])


def run_management_commands():
    manage_script_name = 'manage.py'
    dirs = os.walk('.').next()[1]
    curdir = os.getcwd()
    commands = ['syncdb', 'migrate', 'createsuperuser']

    # With this PR merged, replace this part with simple templating:
    # https://github.com/audreyr/cookiecutter/pull/102
    try:
        for d in dirs:
            os.chdir(d)
            files = os.walk('.').next()[2]
            if manage_script_name in files:
                manage_script_path = os.path.abspath(manage_script_name)
                for c in commands:
                    subprocess.call(['python', manage_script_path, c])
                break
            os.chdir(curdir)
    finally:
        os.chdir(curdir)


def main():
    install_requirements()
    setup_database()
    run_management_commands()

if __name__ == '__main__':
    main()

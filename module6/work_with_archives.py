import shutil


def main():
    # archive_name = shutil.make_archive('backup', 'zip')
    # print(archive_name)

    # archive_name2 = shutil.make_archive('backup2', 'zip', '../Lecture8')
    # print(archive_name2)

    # archive_name3 = shutil.make_archive('backup3', 'zip', '../Lecture9')
    # print(archive_name3)

    # shutil.unpack_archive('backup.zip', '../Lecture8/Unpacked backup')
    print(f'shortcut | description\n---------|-----------------------')
    for shortcut, description in shutil.get_archive_formats():
        print(f'{shortcut:<8} | {description:}')


if __name__ == '__main__':
    main()

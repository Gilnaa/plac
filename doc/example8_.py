# example8_

def main(dsn, command: ("SQL query", 'option', 'c')='select * from table'):
    print('executing %r on %s' % (command, dsn))

if __name__ == '__main__':
    import clap; clap.call(main)

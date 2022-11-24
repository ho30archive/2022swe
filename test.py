def test(a, b);
    if a == b:
        logging.debug('Test succeeded')
        print('True')
    else:
        logging.info('Test failure')
        print('False')
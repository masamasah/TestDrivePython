

def test_tmpdir(tmpdir):
    a_file = tmpdir.join('something.txt')
    a_sub_dir = tmpdir.mkdir('anything')
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write('contents may settle durign shipping')
    another_file.write('something different')

    assert a_file.read() == 'contents may settle durign shipping'
    assert another_file.read() == 'something different'

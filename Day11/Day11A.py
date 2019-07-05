def test_var_args(f_arg, *argv, **kwargs):
    print('First normal arg:', f_arg)
    for arg in argv:
        print('Another arg through *argv:', arg)
    for(key, value) in kwargs.items():
        print(key, value)

test_var_args('Training')
test_var_args('Learning', 'Python', 'Third', 'Day')
test_var_args('Programming', 'Filehandling', 'Python', name = 'Praveen', profession = 'Trainer')
test_var_args('Programming', name = 'Praveen', profession = 'Trainer')

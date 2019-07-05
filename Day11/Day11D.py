def demo_yield():
    print('Code segment1 executed')
    yield 1
    
    print('Code segment2 executed')
    yield 2
    
    print('Code segment3 executed')
    yield 3

    print('Code segment4 executed')

x = demo_yield()
next(x)
    

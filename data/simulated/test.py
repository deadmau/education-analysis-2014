import pickle

try:
    f = open('test.pkl', 'wb')
    text = 'hate:33, college:40, cost:23, shit:20'
    pickle.dump(text, f)
    f.close()

except BaseException:
    pass

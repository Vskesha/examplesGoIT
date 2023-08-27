import pickle


if __name__ == '__main__':
    d = {'test': 12345}
    with open('my_dict.bin', 'wb') as f:
        pickle.dump(d, f)
    d_bytes = pickle.dumps(d)
    print(d_bytes)

    with open('my_dict.bin', 'rb') as f:
        db = pickle.load(f)

    print(db)
    print(pickle.loads(d_bytes))
    

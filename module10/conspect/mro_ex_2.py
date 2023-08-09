# for c in 'ZYXWVUTSRQPONMLKJIHGFEDCBA':
#     print(f"class {c}:\n    def hi(self):\n        print('I am {c} class')\n\n")
class Z:
    # pass
    def hi(self):
        print('I am Z class')


class Y:
    # pass
    def hi(self):
        print('I am Y class')


class X:
    # pass
    def hi(self):
        print('I am X class')


class W:
    # pass
    def hi(self):
        print('I am W class')


class V:
    # pass
    def hi(self):
        print('I am V class')


class U:
    # pass
    def hi(self):
        print('I am U class')


class T:
    # pass
    def hi(self):
        print('I am T class')


class S:
    # pass
    def hi(self):
        print('I am S class')


class R:
    # pass
    def hi(self):
        print('I am R class')


class L:
    # pass
    def hi(self):
        print('I am L class')


class Q(L):
    # pass
    def hi(self):
        print('I am Q class')


class P:
    # pass
    def hi(self):
        print('I am P class')


class O:
    # pass
    def hi(self):
        print('I am O class')


class N:
    # pass
    def hi(self):
        print('I am N class')


class M:
    # pass
    def hi(self):
        print('I am M class')


class K(Y, Z):
    # pass
    def hi(self):
        print('I am K class')


class J(W, X):
    # pass
    def hi(self):
        print('I am J class')


class I(U, V):
    # pass
    def hi(self):
        print('I am I class')


class H(S, T):
    # pass
    def hi(self):
        print('I am H class')


class G(Q, R):
    # pass
    def hi(self):
        print('I am G class')


class F(O, P):
    # pass
    def hi(self):
        print('I am F class')


class E(M, N):
    # pass
    def hi(self):
        print('I am E class')


class D(J, K):
    # pass
    def hi(self):
        print('I am D class')


class C(H, I):
    # pass
    def hi(self):
        print('I am C class')


class B(E, F, G):
    # pass
    def hi(self):
        print('I am B class')


class A(B, C, D):
    # pass
    def hi(self):
        print('I am A class')


if __name__ == '__main__':
    a = A()
    a.hi()
    print(*A.__mro__, sep='\n')

import sax
import numpy as np

tester = {
    ("p1", "p1"): 11,
    ("p1", "p2"): 21,
    ("p2", "p1"): 12,
    ("p2", "p2"): 22,
}

identity = {
    ("p1", "p1"): 0,
    ("p1", "p2"): 1,
    ("p2", "p1"): 1,
    ("p2", "p2"): 0,
}

tester_identity, info = sax.circuit({
    "instances": {
        "test": "tester",
        "ident": "identity",
    },
    "connections": {
        "test,p2": "ident,p1",
    },
    "ports": {
        "in": "test,p1",
        "out": "ident,p2",
    },
}, models={'identity': lambda: identity, 'tester': lambda: tester},
backend="klu"
)

expected = np.array([[11, 12],[21, 22]])

def test_sdense():
    S, pm = sax.sdense(tester)
    assert np.allclose(S, expected)

    S, pm = sax.sdense(tester_identity())
    assert np.allclose(S, expected)




if __name__ == "__main__":
    test_sdense()

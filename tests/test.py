from aerodynamics.aero import airfoil

def test_airfoil():
    # Falta desarrollar tests
    naca = 4412
    dni = "07023193"
    perfil = airfoil(NACA = naca)
    assert(perfil.f == )

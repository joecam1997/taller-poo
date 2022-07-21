class seguridad:
    def __init__(self):
        self.validacion=validacion
        self.clave=clave
        self.usuario=usuario
        self.correo=correo
        self.registro=registro
    def registro(self):
        self.usuario=self.registro
    def validacion(self):
        self.clave=self.usuario
        
class sistema:
    def __init__(self):
        self.prestamos
        self.credito
        self.burodecredito
        self.estadodecuenta
        self.transacciones
        self.solicitudes    
    def mostrar(self):
        print("servicios: {} {} {}".format(self.prestamos,self.credito,self.estadodecuenta,self.transacciones))
        

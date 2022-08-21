from re import S
import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from re import T
from fpdf import FPDF
import csv

pdf = FPDF(orientation='P', unit = 'mm', format = 'A4')
url = 'https://parqueapicola.com/'
        
class PDF(FPDF):
    def header(self):
        #Logo
        self.image('C:/Users/Manuel Castiblanco/Documents/Parque Apícola/Python/Proyecto PCA/imagenes/logo_pca.png', x = 18, y = 10, w = 60, h = 30, link=url)

        #Tipo de letra
        self.set_font('Arial','B',13)
        
        #Title 
        self.multi_cell(w = 235, h = 5, txt = 'PARQUE DE LA CULTURA APÍCOLA \n INVERSIONES AGROTURÍSTICAS EL EDÉN SAS \n GERENCIA DE PARQUE Y ATRACCIONES \n CONFIRMACIÓN RESERVA', border = 0,
                align = 'C', fill = 0)

        #Line break 
        self.ln(5)
        
class pca_GUI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("C:/Users/Manuel Castiblanco/Documents/Parque Apícola/Python/Proyecto PCA/gui_app.ui", self)
        self.boton_generar.clicked.connect(self.fn_cargar)
        
    def fn_cargar(self):
        fecha_pago = self.dateReserva.text()
        num_reserva = self.numReserva.text()
        name_reserva = self.nameReserva.text()
        plan = self.boxPlan.currentText()
        id_reserva = self.idReserva.text()
        celular = self.celularReserva.text()
        fecha_llegada = self.dateLlegada.text()
        fecha_salida = self.dateSalida.text()
        valor_reserva = self.cashReserva.text()
        metodo_pago = self.boxmetodoPago.currentText()
        valorTotal = self.cashtotalReserva.text()
        email = self.email.text()
    
        #Inserción de la clase
        pdf = PDF()
        pdf.alias_nb_pages()

        #margenes
        pdf.set_top_margin(15)
        pdf.set_left_margin(20)
        pdf.set_right_margin(20)

        pdf.add_page()

        #Titles

        pdf.set_font('Arial','B',11)

        pdf.text(x=20, y=55, txt='FECHA DE PAGO DE RESERVA:')
        #pdf.line(82, 55, 110, 55)

        pdf.text(x=120, y=55, txt='NÚMERO DE RESERVA:')
        #pdf.line(167, 55, 190, 55)

        pdf.text(x=20, y=75, txt='NOMBRE DEL TITULAR:') 
        #pdf.line(67, 75, 110, 75)

        pdf.text(x=120, y=75, txt='PLAN:')
        #pdf.line(134, 75, 177, 75)

        pdf.text(x=20, y=80, txt='IDENTIFICACION:   C-')
        #pdf.line(62, 80, 92, 80)

        pdf.text(x=120, y=80, txt='CELULAR:')
        #pdf.line(141, 80, 170, 80)

        pdf.text(x=20, y=85, txt='CORREO ELECTRÓNICO:')
        #pdf.line(69, 85, 120, 85)

        pdf.text(x=20, y=95, txt='FECHA DE LLEGADA:')
        #pdf.line(63, 95, 100, 95)

        pdf.text(x=120, y=95, txt='FECHA DE SALIDA:')
        #pdf.line(158, 95, 190, 95)

        pdf.set_font('Arial','',11)

        pdf.text(x=40, y=100, txt='(CHECK-IN) ')

        pdf.text(x=140, y=100, txt='(CHECK-OUT) ')

        pdf.set_font('Arial','B',11)

        pdf.text(x=20, y=110, txt='VALOR DE RESERVA:  $')
        #pdf.line(68, 110, 100, 110)

        pdf.text(x=120, y=110, txt='FORMA DE PAGO:  $')
        #pdf.line(160, 110, 190, 110)

        pdf.text(x=20, y=115, txt  = 'VALOR TOTAL PLAN:  $')
        #pdf.line(68, 115, 100, 115)

        pdf.text(x=20,y=130, txt='NOTAS IMPORTANTES')

        #________________________________________________________________________________________________________________________________________________________________

        #Inputs

        pdf.set_font('Arial','', 10)

        pdf.text(x=86, y= 55, txt = fecha_pago)
        pdf.text(x=169, y=55, txt = num_reserva)

        pdf.set_font('Arial','', 9)

        pdf.text(x=70, y=75, txt = name_reserva)
        pdf.text(x=73,y=85, txt = email)

        pdf.set_font('Arial','', 10)

        pdf.text(x=138, y=75, txt = plan)
        pdf.text(x=66, y=80, txt = id_reserva)
        pdf.text(x=145, y=80, txt = celular)
        pdf.text(x=67,y=95, txt = fecha_llegada)
        pdf.text(x=162,y=95, txt = fecha_salida)
        pdf.text(x=72,y=110, txt = valor_reserva)
        pdf.text(x=164,y=110, txt = metodo_pago)
        pdf.text(x=72,y=115,txt = valorTotal)


        pdf.set_font('Arial','',10)

        pdf.text(x=20,y=135, txt='LA UBICACIÓN DEL PARQUE APÍCOLA ES EN SILVANIA, CUNDINAMARCA - VEREDA SAN')

        pdf.text(x=20,y=139, txt='LUIS BAJO TEL: 316 8303491 -  315 3880798 ')

        pdf.text(x=20,y=144, txt='1. La entrega de las habitaciones se hará a partir de las 3:00 PM (Check-In). ')

        pdf.text(x=20,y=150, txt='2. La hora de entrega de habitación por parte del huésped (Check-Out) es a la 12:00 M. Si el ')

        pdf.text(x=20,y=154, txt='huésped desea hacer heck-out posterior a esta hora deberá consultar con la recepción la')

        pdf.text(x=20,y=158, txt='disponibilidad y pagar un cargo adicional equivalente al 50% de la tarifa diaria, tendrá hasta las')

        pdf.text(x=20,y=162, txt='4:30 PM para hacer entrega de alojamiento. ')

        pdf.text(x=20,y=168, txt='3. No se realizan reembolsos de ninguna índole, el costo de penalidad por modificación de fecha')

        pdf.text(x=20,y=172, txt='inicial reservada es del 10% del valor del plan pagado.')

        pdf.text(x=20,y=178, txt='4. El pago de la totalidad del plan se debe realizar al momento de ingresar a las instalaciones del')

        pdf.text(x=20,y=182, txt='Parque.')

        pdf.text(x=20,y=188, txt='5. La entrega de la llave del alojamiento tiene un valor depósito de $10.000 pesos COP, por')

        pdf.text(x=20,y=192, txt='seguridad en caso de perdida.')

        pdf.text(x=20,y=198, txt='6. Todo visitante que se encuentre en las instalaciones del Parque acepta implícitamente que')

        pdf.text(x=20,y=202, txt='se le realice contenido fotográfico y fílmico para fines comerciales y publicitarios, a menos que')

        pdf.text(x=20,y=206, txt='presente un documento que manifieste inconformidad.')

        pdf.text(x=20,y=212, txt='7. El valor pagado está sujeto a validación por el parque el día de Check-In. En caso de identificar')

        pdf.text(x=20,y=216, txt='alguna diferencia en la  liquidación inicial de la reserva, se procederá con el ajuste correspondiente')

        pdf.text(x=20,y=220, txt='y el cliente deberá asumir el valor que le  corresponda. El pago de la totalidad del plan se debe')

        pdf.text(x=20,y=224, txt='realizar al momento de ingresar a las instalaciones del Parque.')

        pdf.text(x=20,y=230, txt='8. Todo niño con 6 años cumplidos, debe cancelar tarifa plena puesto que a esta edad puede hacer')

        pdf.text(x=20,y=234, txt='uso y goce de todas las atracciones.')

        pdf.text(x=20,y=240, txt='9. Todos los huéspedes (adultos y menores de edad) deberán presentar su documento de identificación en el')

        pdf.text(x=20,y=244, txt='Check-in sin  excepción. Si viaja con menores de 18 años de edad, debe garantizar que se hospedarán')

        pdf.text(x=20,y=248, txt='únicamente con sus padres.')

        pdf.text(x=20,y=254, txt='10. La explotación, la pornografía y el turismo sexual con menores están prohibidos y penalizados.')

        pdf.text(x=20,y=258, txt='Ley 679 agosto 2001.')

        pdf.text(x=20,y=264, txt='El Parque de la cultura Apicola protege los datos de visitantes acorde a la Ley 1581 del 2012 y el Decreto')

        pdf.text(x=20,y=268, txt='No. 1377 del 2013. Solicita autorizar el tratamiento de sus datos personales con el fin de hacer uso de los')

        pdf.text(x=20,y=272, txt='para los fines de su reserva hotelera.')

        pdf.set_font('Arial','I',11)

        pdf.text(x=58,y=282, txt= 'Te invitamos a tener en cuenta estas recomendaciones y esperamos')

        pdf.text(x=65,y=286, txt='disfrutes al máximo tu visita al PRIMER PARQUE APÍCOLA')

        pdf.text(x=92,y=290, txt='EN COLOMBIA')

        #RECTANGULOS

        pdf.rect(x=15,y=45,w=180,h=16)

        pdf.rect(x=15,y=65,w=180,h=55)

        pdf.rect(x=15,y=125,w=180,h=150)

        #QR

        pdf.image('C:/Users/Manuel Castiblanco/Documents/Parque Apícola/Python/Proyecto PCA/imagenes/qr_pca.jpg',x=37,y=276,w=20,h=20)

        # pdf.multi_cell

        pdf.output("Reserva #" + str(num_reserva) + ".pdf", 'F')
        print("Confirmación generada")
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = pca_GUI()
    GUI.show()
    sys.exit(app.exec_())
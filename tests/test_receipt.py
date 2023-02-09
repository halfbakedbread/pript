from pript import pript


def draw_receipt():
  pript(sep='*')
  pript('HalfBakedCoffee Company', pos='center')
  pript('014210 Half Baked Ave.', pos='center')
  pript(' Receipt ', pos='center', sep="*")
  pript('Date: ', ' 04/02/2023 11:54:02')
  pript()
  pript(' Item list ', pos='center', sep="*")
  pript('Item: ', ' Big Coffee')
  pript('Quantity: ', ' 2')
  pript('Price: ', ' $5.00', sep='.')
  pript()
  pript(sep="*")
  pript('Item: ', ' Small Coffee')
  pript('Quantity: ', ' 2')
  pript('Price: ', ' $2.50', sep='.')
  pript()
  pript(sep="*")
  pript('Total: ', ' $15.00', sep='.')
  pript('Paid: ', ' $15.00', sep='.')
  pript('Thank you! ', ' Mr. Buyer')
  pript(sep='*')


if __name__ == '__main__':
    draw_receipt()

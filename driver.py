from geopy.distance import vincenty
from delivery  import Delivery
from executive import Executive
from order import Order
import yaml

def simple_scoring_func(de, order):
    # use vincenty distance and inverse it to give a score
    return  1000 - vincenty(de.get_latlong(),order.get_latlong()).km


if __name__ == "__main__":
    delivery_execs = []
    orders = []

    with open("conf.yaml", 'r') as stream:
        try:
            conf = yaml.load(stream)
            for d in conf["de"]:
                delivery_execs.append(Executive(d['id'], d['lat'], d['long']))
            for o in conf["orders"]:
                orders.append(Order(o['id'], o['lat'], o['long'], o['value']))
        except Exception as exc:
            print(exc)
            exit(1)



    # delivery_execs = [(12.9279232, 77.6271078), (12.92488806, 77.64945745)]
    # orders = [(12.92279665, 77.65190363), (12.92965641, 77.62925506)]

    driver = Delivery(delivery_execs, orders, simple_scoring_func)
    assignment, score = driver.assign()
    for d,o in assignment.iteritems():
        print d.id + "->" + o.id
    print score

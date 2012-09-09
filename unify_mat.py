import c4d
from c4d import gui
from c4d import documents
#Welcome to the world of Python


def main():
    # gui.MessageDialog('Hello GUI World!')
    # print "Hello console World!"
    # watch out 'GetActiveObject()' is deprecated
    doc = documents.GetActiveDocument()

    # print "%r" % doc.GetSelection()
    for obj in doc.GetSelection():
        # c4d.BaseObject object called 'Licht/Licht'
        # with ID 5102 at 0x112971150
        # print '%r' % obj.GetTypeName()
        # if obj.GetTypeName() == 'Polygon-Objekt':
        # print obj

        if isinstance(obj, c4d.TextureTag):
            print 'Got a BaseMaterial called %r %r' % (obj.GetTypeName(), obj.GetName())

        if isinstance(obj, c4d.PolygonObject):
            print '%r %r' % (obj.GetTypeName(), obj.GetName())


if __name__ == '__main__':
    main()

from quickstart import create_service


service = create_service()

class user:

    def __init__(self):
        print('User created')

    def find_labelid(self, name):
        try:
            obj = service.users().labels().list(userId='me').execute()
            names = [label['name'] for label in obj['labels']]
            labelids = [label['id'] for label in obj['labels']]

            if name in names:
                print('Found label: %s with labelid: %s' % (name, labelids[names.index(name)]))
            else:
                print('Label with name: %s not found' % (name))

            return labelids[names.index(name)]

        except Exception as error:
            print('An error occurred while creating label: %s' % error)
            return None
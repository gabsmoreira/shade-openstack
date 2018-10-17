from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

instance_id = '7f748509-a58f-4d03-9aac-2b1f521ace6c'

conn.delete_server(name_or_id=instance_id)


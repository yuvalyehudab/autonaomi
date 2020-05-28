#database.py
#utils.database
import pymongo
import datetime

class mongo:
  def __init__(self, host, port):
    self.client = pymongo.MongoClient(host=host, port=port)
    self.db = self.client.db

  def save(self, user_info, snapshot_id, data):

    query = {'user_id': user_info.user_id}
    if not self.db.users.find_one(query):
      self.db.users.insert_one({
        'user_id': user_info.user_id,
        'username': user_info.username,
        'birthday': user_info.birthday,
        'gender': user_info.gender
        })
    query['snapshot_id'] = snapshot_id
    if not self.db.snapshots.find_one(query):
      self.db.snapshots.insert_one(query)
    self.db.snapshots.find_one_and_update(query, {'$set': data})

  def get_user(self, user_id):
    
    document = self.db.users.find_one({'user_id': int(user_id)})
    if not document:
      
      return {}
    return {
            "user_id": document["user_id"],
            "username": document["username"],
            "birthday": f'{datetime.datetime.fromtimestamp(document["birthday"]):%Y/%m/%d}',
            "gender": document["gender"],
        }

  def get_users(self):
    res = []
    for d in self.db.users.find():
      res.append({
        'user_id': d['user_id'],
        'username': d['username']
        })
    return res

  def get_result(self, user_id, snapshot_id, result_name):
    q = {'user_id': int(user_id), 'snapshot_id': int(snapshot_id)}
    d = self.db.snapshots.find_one(q)
    
    if not d:
      return {}
    return d[result_name]

  def get_snapshot(self, user_id, snapshot_id):
    q = {'user_id': int(user_id), 'snapshot_id': int(snapshot_id)}
    d = self.db.snapshots.find_one(q)
    if not d:
      return {}

    t = d['snapshot_id']
    s = datetime.datetime.fromtimestamp(t/1000)
    res = {
    'snapshot_id': t,
    'timestamp': f'{s:%Y/%m/%d %H:%M:%S}',
    'available results': [x for x in d if not x == 'user_id' and not x == 'snapshot_id' and not x == '_id']
    }
    return res

  def get_snapshots(self, user_id):
    res = []
    q = {'user_id': int(user_id)}

    for d in self.db.snapshots.find(q):
      t = d['snapshot_id']
      s = datetime.datetime.fromtimestamp(t/1000)
      res.append({'snapshot_id': t, 'timestamp': f'{s:%Y-%m-%d %H-%M-%S-%f}'})

    return res

  def clear_all(self):
    self.db.collection.remove({})





class database:
  schemes = {'mongodb': mongo}
  def __init__(self, scheme, host, port):
    if scheme not in self.schemes:
      raise
    self.con = self.schemes[scheme](host=host, port=port)

  def save(self, user_info, snapshot_id, data):
    self.con.save(user_info, snapshot_id, data)

  def get_user(self, user_id):
    return self.con.get_user(user_id)

  def get_users(self):
    return self.con.get_users()

  def get_snapshot(self, user_id, snapshot_id):
    return self.con.get_snapshot(user_id, snapshot_id)

  def get_snapshots(self, user_id):
    return self.con.get_snapshots(user_id)

  def get_result(self, user_id, snapshot_id, result_name):
    return self.con.get_result(user_id, snapshot_id, result_name)

  def clear_all(self):
    self.con.clear_all()



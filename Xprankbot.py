#FROM X_PRES WITH OPEN SQL
#MULTY PROSESING

settingsOpen = codecs.open("Xline.json","r","utf-8")
set = json.load(settingsOpen)
me = LINE()
me.log("TOKEN: " + str(me.authToken))
channelToken = me.getChannelResult()
channel = Channel(me, me.server.CHANNEL_ID['LINE_MUSIC'])
def backupData():
    try:
        backup = set
        f = codecs.open('Xline.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def X_pres(text):
    R_sQL = text.lower()
    if set["key"] == True:
        if R_sQL.startswith(set["text"]):
            Pbot = R_sQL.replace(set["text"],"")
        else:
            Pbot = "sprin X_pres"
    else:
        Pbot = text.lower()
    return Pbot
def bot(op):
    global time
    global ast
    global groupParam
    global multiprocessing
    global subprocess
    global threading
    try:
        if op.type == 0:
            return
        if op.type == 25:
          if set["bot"] == True:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            R = msg.to
            D = msg._from
            key = set["text"].title()
            if set["key"] == False:
                 key = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if D != me.profile.mid:
                        to = D
                    else:
                        to = R
                elif msg.toType == 1:
                    to = R
                elif msg.toType == 2:
                    to = R
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        Pbot = X_pres(text)
                        return
        if op.type == 5:
            return
        if op.type == 11:
            return
        if op.type == 13:
            return
        if op.type == 15:
            return
        if op.type == 17:
            return
        if op.type == 19:
            return
        if op.type == 32:
            return
        if op.type == 46:
            return
        if op.type == 55:
            return
    except Exception as error:
        logError(error)
        if op.type == 59:
            print (op)
 
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        me.log("Eror: " + str(e))

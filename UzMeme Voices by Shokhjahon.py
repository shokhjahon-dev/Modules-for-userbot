#
#░██████╗██╗░░██╗░█████╗░██╗░░██╗██╗░░██╗░█████╗░
#██╔════╝██║░░██║██╔══██╗██║░██╔╝██║░░██║██╔══██╗
#╚█████╗░███████║██║░░██║█████═╝░███████║███████║
#░╚═══██╗██╔══██║██║░░██║██╔═██╗░██╔══██║██╔══██║
#██████╔╝██║░░██║╚█████╔╝██║░╚██╗██║░░██║██║░░██║
#╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
#
#
#
#             © Copyright 2022
#
#          https://t.me/abdukhalimov_sh
#
#  Licensed under the GNU GPLv3
#  https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @abdukhalimov_sh
#
# voicelarni yolg'iz yoki quloqchin(naushnik)larda eshitish tavsiya etiladi. Bularni birovni kamsitish uchun ishlatmang. Bu hazil tariqasida ishlangan!

from .. import loader, utils 
from asyncio import sleep 

 
def register(cb): 
 cb(VoicesUzMod()) 
  
class VoicesUzMod(loader.Module): 
 """Voices list""" 
  
 strings = { "name": "UzMemes" } 

 async def ukajonimcmd(self, message): 
  """Ukajonim meme""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/5", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def iyecmd(self, message): 
  """iye meme""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/6", voice_note=True, reply_to=reply.id if reply else None) 
  return 
   
 async def bilasanmicmd(self, message): 
  """isqirt meme""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/7", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def slabiycmd(self, message): 
  """music on giorno's theme""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/8", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def darknetcmd(self, message): 
  """chala minor ponyatka""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/9", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def sekscmd(self, message): 
  """meme seks""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/10", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def kotcmd(self, message): 
  """meme kot""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/12", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def jonborcmd(self, message): 
  """meme jonbor""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/13", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
  
 async def detskiycmd(self, message): 
  """meme detskiy""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/14", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def nmagapgrcmd(self, message): 
  """nma gap gr""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/15", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def prezidentcmd(self, message): 
  """saviyang yoq""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/16", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def ebsancmd(self, message): 
  """Qota*imni ebsan""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/51", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def akacmd(self, message): 
  """Aka unday demang"""
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/52", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def movecmd(self, message): 
  """ебааать""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/53", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def baqirmacmd(self, message): 
  """baqirma""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/54", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def uzrcmd(self, message): 
  """vay vay uzur ketib qobti""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/55", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def tiqdincmd(self, message): 
  """shuncha qiganimni""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/18", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def aufcmd(self, message): 
  """auf""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/2", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def bahorlardacmd(self, message): 
  """bekcore bahorlarda""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/4", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def oxblecmd(self, message): 
  """oox blee""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/5", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def byaqqacmd(self, message): 
  """byaqqa ciqqin when I was king)""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/6", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def salomalekumcmd(self, message): 
  """Gruppa""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/7", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def guccicmd(self, message): 
  """Gucci flip flap""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/8", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def likebosingcmd(self, message): 
  """like boosingg""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/9", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def mazzamicmd(self, message): 
  """mazzami silaga""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/10", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def nmagapcmd(self, message): 
  """Nmaa gaap""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/11", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def omagatcmd(self, message): 
  """ooo magat""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/12", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def poxuycmd(self, message): 
  """Poxuy poxuy poxuy ...18+""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/13", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def ban1cmd(self, message): 
  """pubg ban""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/14", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def seks1cmd(self, message): 
  """seks koryabsanmi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/15", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def manovinicmd(self, message): 
  """shu gapizga""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/16", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def theendcmd(self, message): 
  """The end """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/17", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def tugadicmd(self, message): 
  """tugadi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/19", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def eytoxtacmd(self, message): 
  """ey toxta sen ey""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/20", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def telecomcmd(self, message): 
  """uztelecom""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/21", voice_note=True, reply_to=reply.id if reply else None) 
  return 
  
 async def maladescmd(self, message): 
  """vapwi malades""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/22", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def tobaqldmcmd(self, message): 
  """toba qildm""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/23", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def qiwloqcmd(self, message): 
  """qiwloq sokin""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/24", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def yoqoolcmd(self, message): 
  """Yoqool""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/25", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def sokinkuliwcmd(self, message): 
  """sokin kuliw""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/26", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def bskcmd(self, message): 
  """bugun sening kuning""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/27", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def keyncicmd(self, message): 
  """innan keyinci""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/28", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def soqqacmd(self, message): 
  """Bos soqqani uka""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/29", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def tfuszgacmd(self, message): 
  """Tupurdim sizga""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/30", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def echichqoqcmd(self, message): 
  """ie chichqoq""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/31", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def pshnxcmd(self, message): 
  """pawol naxxuy""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/32", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def blaacmd(self, message): 
  """blyaaa""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/33", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def nervinnicmd(self, message): 
  """san nervinni ekansanu""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/34", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def shiltacmd(self, message): 
  """shu shilta yoqmayabdida""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/35", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def yuyuyucmd(self, message): 
  """yuyuyuyu""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/36", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def akajonimcmd(self, message): 
  """akajonim meni mehribonim""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/37", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def orqamiyyacmd(self, message): 
  """orqa miyyenga shapalo uraman uka""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/38", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def xuyetqvosamicmd(self, message): 
  """xuyet qvosanmi o dabba""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/39", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def oneni18cmd(self, message): 
  """oneni horlab ske""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/40", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def uzoqqasyiwcmd(self, message): 
  """ortogin bn borib km uzoqqa syiw oynagn""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/41", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def nmagap18cmd(self, message): 
  """nma gap qanchula""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/42", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def maqsadcmd(self, message): 
  """maqsad sek*""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/43", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def kurs200cmd(self, message): 
  """200$ 2million 700""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/44", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def garikcmd(self, message): 
  """man na*uy vorzakonman""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/45", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def eyqotagimcmd(self, message): 
  """multik""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/46", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def kotizisotincmd(self, message): 
  """kotizi sotin jalab stulda otirganizda teks otiras""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/47", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def yaxweecmd(self, message): 
  """yaxweee""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/48", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def erkakbocmd(self, message): 
  """erkak bo jalab""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/49", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def pitirpitircmd(self, message): 
  """ptr ptr ptr ptr *miga scqon tqadi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/50", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def qotogmalvidocmd(self, message): 
  """qotogm qotogm alvidoo senga""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/51", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def naxuynenujencmd(self, message): 
  """ты мне нахуй не нужен""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/52", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def unademencmd(self, message): 
  """aka una demen endi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/53", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def tt10kcmd(self, message): 
  """agar ttda 10k patpischigim bosa chochagimi tegidan uzvoraman""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/54", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def laychacmd(self, message): 
  """laycha laycha""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/55", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def qotaqtelecomcmd(self, message): 
  """qo*aqtelecom qliw kere""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/56", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def mnepoxuycmd(self, message): 
  """да мне похуй""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/57", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def sqamacmd(self, message): 
  """s*aman hoziii""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/58", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def poxxuymasmicmd(self, message): 
  """sanga poxxuymasmi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/59", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def wampanskicmd(self, message): 
  """Enangni omiga wampansky tqama""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/60", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def miyyengacmd(self, message): 
  """miyyenga qotagim dalbayob qozivoy""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/61", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def cozaxuynacmd(self, message): 
  """cho za xuyna""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/62", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def ulanvolbcmd(self, message): 
  """aka kmdur ulanvolb sokinyabdi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/63", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def music18cmd(self, message): 
  """oneni ami dadeni ami""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/64", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def birikkiuchcmd(self, message): 
  """1-2-3 oneyni *mi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/65", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def syibqoyamancmd(self, message): 
  """jala hoz syib qoyama""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/66", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def qotaqbascmd(self, message): 
  """ha qotaqbas""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/67", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def burnizgaskamacmd(self, message): 
  """ogzi burniga skama burnizdan burnizdan kopi keladi koziz qzaradi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/68", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def corniqilcmd(self, message): 
  """yoqmasa chorni ql xaromi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/69", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def negacmd(self, message): 
  """negaaa""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/70", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def nmaladeyabsancmd(self, message): 
  """nmalar deyabsan o'zingdan o'zing""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/71", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def suvgasolcmd(self, message): 
  """qotagin qicigan bosa suv puvga solov""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/72", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def shoxcmd(self, message): 
  """shoxlaga maza db oylisla""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/73", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def sikvoramanborucmd(self, message): 
  """dalbancha sokiniw""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/74", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def pornhubcmd(self, message): 
  """pornhub intro ogg""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/75", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def orginalcmd(self, message): 
  """orginalmi bu obb""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/76", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def xaymicmd(self, message): 
  """e dalbayob karochi uxlading xaymi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/77", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def tqdinjorajoncmd(self, message): 
  """pubg deb skilgan bola""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/78", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def uchinchisinfcmd(self, message): 
  """uzbek sila bla 3 chi sinfman""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/79", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def soskacmd(self, message): 
  """oneni amiga tqib qoyaman soska""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/81", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def iloncmd(self, message): 
  """kotingga ilon krib ketsin""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/82", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def sadidancmd(self, message): 
  """3 minutli prikol sadidan""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/84", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def sherniyomonicmd(self, message): 
  """toying kuni talpada qoldim""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/85", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def dabbacmd(self, message): 
  """xapa bomangu girt dabba bolekansz""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/86", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def yoryorcmd(self, message): 
  """yor yor""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/87", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def viuviucmd(self, message): 
  """ dedida pax dedida varrr etib...""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/88", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def ahhhcmd(self, message): 
  """голос от камол (18+)""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/89", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def oqicmd(self, message): 
  """ewwak oqi gandon""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/90", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def rep1cmd(self, message): 
  """onagni ami dadangni ami""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/91", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def yaxaytcmd(self, message): 
  """yaxayt onagni ske - bekcore""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/92", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def tobaqildmcmd(self, message): 
  """toba qildim astafilla""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/93", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def maqtovcmd(self, message): 
  """maqtov yorligi berila""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/94", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def yorvoramancmd(self, message): 
  """yorvoraman kotini ukam oynawasan batta""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/95", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def shampuncmd(self, message): 
  """shampun junbaysinba""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/96", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def gomegomecmd(self, message): 
  """India music gome gome""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/97", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def yozma2cmd(self, message): 
  """Yozma Manga""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/138", voice_note=True, reply_to=reply.id if reply else None) 
  return 
   
 async def privetcmd(self, message): 
  """Ты игноришь мине, когда тибе пишу""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/132", voice_note=True, reply_to=reply.id if reply else None) 
  return
 
 async def benzemacmd(self, message): 
  """Шешенгдын амы бензема""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/133", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def aminiqscmd(self, message): 
  """amini qsib tur yban""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/135", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def kechacmd(self, message): 
  """Brinchi Kecha """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/134", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def cozahuynacmd(self, message): 
  """Coza Huyna Aslmaboi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/136", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def shahnozcmd(self, message): 
  """Ya Tvoy micro yebal Shahnoz"""
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/137", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def pulcmd(self, message): 
  """pul gapirganda haqiqat jim turadi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/105", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def trendcmd(self, message): 
  """Tik Tok trend""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/106", voice_note=True, reply_to=reply.id if reply else None) 
  return
 
 async def nigohsizsexcmd(self, message): 
  """TT trend""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/107", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def nega2cmd(self, message): 
  """Negaaa""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/108", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def buvinicmd(self, message): 
  """buvini ami """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/109", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def viucmd(self, message): 
  """viu viu dedida paq dedida varr etib """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/110", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def siucmd(self, message): 
  """ronaldo xuykalla""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/111", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def dunyocmd(self, message): 
  """eee dunyo seni togangmas yo amakivachchangmas doim qarab konglingga otang yoki onangmas""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/112", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def manxcmd(self, message): 
  """Ma naxuy - aslamboi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/113", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def ioneynicmd(self, message): 
  """i onangni ski - aslamboi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/114", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def talabacmd(self, message): 
  """4 yil umrizi xazon qvotganiz bilan tabrikliman - motiv bekcore""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/115", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def solocmd(self, message): 
  """prosta solo prosta solo""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/116", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def choqcmd(self, message): 
  """choq 100$ choq 200$ baq 500$""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/117", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def onayniskicmd(self, message): 
  """when I was king""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/118", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def idinxtogdacmd(self, message): 
  """ne lyubiw idi naxuy togda """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/119", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def jonimcmd(self, message): 
  """jonimm - aslamboi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/120", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def weecmd(self, message): 
  """wee come to far...""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/121", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def lovelycmd(self, message): 
  """music lovely""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/122", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def music0cmd(self, message): 
  """qanaqadir music""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/123", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def music1cmd(self, message): 
  """qanaqadir musica 1""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/124", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def lalalacmd(self, message): 
  """lalala lalalala """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/125", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def ixixixicmd(self, message): 
  """smex umar - ixixixi """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/126", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def uwucmd(self, message): 
  """uvev""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/127", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def ayycmd(self, message): 
  """baqiriwni biri""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/128", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def hacortcmd(self, message): 
  """ha cort nma gap""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/129", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def hakotlacmd(self, message): 
  """ha kotla qalesila""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/130", voice_note=True, reply_to=reply.id if reply else None) 
  return


 async def arabiccmd(self, message): 
  """music arabic """ 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/131", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def vayjalacmd(self, message): 
  """brat""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/140", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def dalbayobsancmd(self, message): 
  """dalbayobsaan music""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/141", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def seksvaqticmd(self, message): 
  """dostlar strimni ochiryabmiz chunki seks vaqti keldi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/142", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def korsincmd(self, message): 
  """kozzi qotoga berib qoymagan bilsin oqisin korsin degan""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/143", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def buvinicmd(self, message): 
  """buvini ami - avtobuschi oka""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/ShokhMemes/144", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def _directed(self, message): 
  """giorno's theme inform""" 
   
  hey = """ 
<b>🐝 Directed by Robert B. YouTube link:</b> https://youtu.be/_UOzcZbqwig""" 
  await message.edit(hey) 
   
 async def _giorno(self, message): 
  """giorno's theme inform""" 
   
  hey = """ 
<b>🐝 Giorno's Theme. YouTube link:</b> https://youtu.be/WuiY_f0NUzE""" 
  await message.edit(hey) 
   
 async def _toby(self, message): 
  """toby fox inform""" 
   
  hey = """ 
<b>🐝 Toby Fox - Fallen Down. YouTube link:</b> https://youtu.be/cGBMTAGzWPs""" 
  await message.edit(hey) 
   
 async def _rick(self, message): 
  """toby fox inform""" 
   
  hey = """ 
<b>🐝 Rick Roll - Never Gonna Give You Up. YouTube link:</b> https://youtu.be/dQw4w9WgXcQ""" 
  await message.edit(hey) 
   
 async def _putin(self, message): 
  """toby fox inform""" 
   
  hey = """ 
<b>🐝 Wide Putin Walk. YouTube link:</b> https://youtu.be/Wl959QnD3lM""" 
  await message.edit(hey) 
  
 async def _singlil(self, message): 
  """toby fox inform""" 
   
  hey = """ 
<b>🍂 Sing lil link:</b> https://youtu.be/Wl959QnD3lM""" 
  await message.edit(hey) 
  
 async def voicescm_(self, message): 
  """general voices list""" 
   
  await self.inline.form( 
                    self.strings("main", message), 
                    reply_markup=[ 
                     [{ 
       "text": "🐝 Directed by",  
       "callback": self._directed 
      }], 
                     [{ 
       "text": "🦁 Giorno's Theme",  
       "callback": self._giorno 
      }], 
                     [{ 
       "text": "🦥 Toby Fox",  
       "callback": self._toby 
      }], 
                        [{ 
       "text": "🐱 Rick Roll",  
       "callback": self._rick 
      }], 
                        [{ 
       "text": "🐎 Wide Putin",  
       "callback": self._putin 
       }],                      
                        [{ 
       "text": "🌌 Sing Lil",  
       "callback": self._singlil 
       }],                         
                    ], 
                    ttl=10, 
                    message=message, 
                ) 
 
 async def oqicmd(self, message): 
  """Oqi gand""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/39", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def uryapticmd(self, message): 
  """Mana meni urapaypt""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/40", voice_note=True, reply_to=reply.id if reply else None) 
  return 
   
 async def blaacmd(self, message): 
  """Ox blaa""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/46", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def jinnilicmd(self, message): 
  """Jinnili boshlandi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/47", voice_note=True, reply_to=reply.id if reply else None) 
  return 
 
 async def jumacmd(self, message): 
  """Juma Muborak""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/43", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def rasmgaolcmd(self, message): 
  """Rasmga ol""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/45", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def kotcmd(self, message): 
  """meme kot""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/12", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def vorzakonmancmd(self, message): 
  """Garik Vondiy""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/48", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
  
 async def switchupcmd(self, message): 
  """Switch up""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/49", voice_note=True, reply_to=reply.id if reply else None) 
  return
  
 async def towbaqacmd(self, message): 
  """Towbaqa uchadi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/50", voice_note=True, reply_to=reply.id if reply else None) 
  return
    
 async def miyyengacmd(self, message): 
  """Miyyenga q***""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/36", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def buvinicmd(self, message): 
  """Senator meme""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/36", voice_note=True, reply_to=reply.id if reply else None) 
  return

 async def bilasizlarmicmd(self, message): 
  """Bilasizlarmi""" 
 
  reply = await message.get_reply_message() 
  await message.delete() 
  await message.client.send_file(message.to_id, "https://t.me/VoiceAmore/42", voice_note=True, reply_to=reply.id if reply else None) 
  return
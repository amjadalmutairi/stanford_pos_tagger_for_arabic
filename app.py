from nltk import StanfordPOSTagger

text = ''' الفيتامينات هي عناصر غذائيّة أساسية لجسم الإنسان، وهي عبارة عن مركبات عضويّة توجد طبيعيّاً في الأغذية ويحتاجها الجسم بكميّات بسيطة 
للقيام بوظائفه الطبيعية، ولا يستطيع الجسم تصنيعها أو تصنيع كميّات كافية منها لتلبي احتياجاته'''

Tagger = StanfordPOSTagger('./stanfor arabic modeal and tagger/arabic.tagger', './stanfor arabic modeal and tagger/stanford-postagger.jar')
output = Tagger.tag(text.split())
output = [tuple(filter(None, tp)) for tp in output] #remove empty tubles

for data in output:
	print(data[0].split("/")[0] + " > " + data[0].split("/")[1] + "\n" )

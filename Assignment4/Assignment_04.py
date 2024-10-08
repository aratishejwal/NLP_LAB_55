###  Assignment No 4 ###

"""Assignment Title : Implement Bi-gram, Tri-gram word sequence and its count in text input
data using NLTK library"""


from nltk import ngrams
from nltk.util import ngrams

#unigram model
n = 1
sentence = 'Ratan Naval Tata (born 28 December 1937) is an Indian industrialist, philanthropist and former chairman of Tata Sons. He was a chairman of the Tata Group from 1990 to 2012, and interim chairman from October 2016 through February 2017. He continues to head its charitable trusts.In 2008, he received the Padma Vibhushan, the second highest civilian honour in India, after receiving the Padma Bhushan, the third highest civilian honour in 2000.He is the son of Naval Tata, who was adopted by Ratanji Tata, son of Jamsetji Tata, the founder of the Tata Group.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   UNIGRAM    ************************")
for item in unigrams:
    print(item)
#bigram model
n = 2
sentence = 'Ratan Naval Tata (born 28 December 1937) is an Indian industrialist, philanthropist and former chairman of Tata Sons. He was a chairman of the Tata Group from 1990 to 2012, and interim chairman from October 2016 through February 2017. He continues to head its charitable trusts.In 2008, he received the Padma Vibhushan, the second highest civilian honour in India, after receiving the Padma Bhushan, the third highest civilian honour in 2000.He is the son of Naval Tata, who was adopted by Ratanji Tata, son of Jamsetji Tata, the founder of the Tata Group.'

unigrams = ngrams(sentence.split(), n)
print(f"\n***********   BIGRAM    ************************")
for item in unigrams:
    print(item)

#trigram model
n = 3
sentence = 'Ratan Naval Tata (born 28 December 1937) is an Indian industrialist, philanthropist and former chairman of Tata Sons. He was a chairman of the Tata Group from 1990 to 2012, and interim chairman from October 2016 through February 2017. He continues to head its charitable trusts.In 2008, he received the Padma Vibhushan, the second highest civilian honour in India, after receiving the Padma Bhushan, the third highest civilian honour in 2000.He is the son of Naval Tata, who was adopted by Ratanji Tata, son of Jamsetji Tata, the founder of the Tata Group.'
unigrams = ngrams(sentence.split(), n)
print(f"\n***********   TRIGRAM    ************************")
for item in unigrams:
    print(item)

'''
Output
***********   UNIGRAM    ************************
('Ratan',)   
('Naval',)   
('Tata',)    
('(born',)   
('28',)      
('December',)
('1937)',)   
('is',)      
('an',)
('Indian',)
('industrialist,',)
('philanthropist',)
('and',)
('former',)
('chairman',)
('of',)
('Tata',)
('Sons.',)
('He',)
('was',)
('a',)
('chairman',)
('of',)
('the',)
('Tata',)
('Group',)
('from',)
('1990',)
('to',)
('2012,',)
('and',)
('interim',)
('chairman',)
('from',)
('October',)
('2016',)
('through',)
('February',)
('2017.',)
('He',)
('continues',)
('to',)
('head',)
('its',)
('charitable',)
('trusts.In',)
('2008,',)
('he',)
('received',)
('the',)
('Padma',)
('Vibhushan,',)
('the',)
('second',)
('highest',)
('civilian',)
('honour',)
('in',)
('India,',)
('after',)
('receiving',)
('the',)
('Padma',)
('Bhushan,',)
('the',)
('third',)
('highest',)
('civilian',)
('honour',)
('in',)
('2000.He',)
('is',)
('the',)
('son',)
('of',)
('Naval',)
('Tata,',)
('who',)
('was',)
('adopted',)
('by',)
('Ratanji',)
('Tata,',)
('son',)
('of',)
('Jamsetji',)
('Tata,',)
('the',)
('founder',)
('of',)
('the',)
('Tata',)
('Group.',)

***********   BIGRAM    ************************
('Ratan', 'Naval')
('Naval', 'Tata')
('Tata', '(born')
('(born', '28')
('28', 'December')
('December', '1937)')
('1937)', 'is')
('is', 'an')
('an', 'Indian')
('Indian', 'industrialist,')
('industrialist,', 'philanthropist')
('philanthropist', 'and')
('and', 'former')
('former', 'chairman')
('chairman', 'of')
('of', 'Tata')
('Tata', 'Sons.')
('Sons.', 'He')
('He', 'was')
('was', 'a')
('a', 'chairman')
('chairman', 'of')
('of', 'the')
('the', 'Tata')
('Tata', 'Group')
('Group', 'from')
('from', '1990')
('1990', 'to')
('to', '2012,')
('2012,', 'and')
('and', 'interim')
('interim', 'chairman')
('chairman', 'from')
('from', 'October')
('October', '2016')
('2016', 'through')
('through', 'February')
('February', '2017.')
('2017.', 'He')
('He', 'continues')
('continues', 'to')
('to', 'head')
('head', 'its')
('its', 'charitable')
('charitable', 'trusts.In')
('trusts.In', '2008,')
('2008,', 'he')
('he', 'received')
('received', 'the')
('the', 'Padma')
('Padma', 'Vibhushan,')
('Vibhushan,', 'the')
('the', 'second')
('second', 'highest')
('highest', 'civilian')
('civilian', 'honour')
('honour', 'in')
('in', 'India,')
('India,', 'after')
('after', 'receiving')
('receiving', 'the')
('the', 'Padma')
('Padma', 'Bhushan,')
('Bhushan,', 'the')
('the', 'third')
('third', 'highest')
('highest', 'civilian')
('civilian', 'honour')
('honour', 'in')
('in', '2000.He')
('2000.He', 'is')
('is', 'the')
('the', 'son')
('son', 'of')
('of', 'Naval')
('Naval', 'Tata,')
('Tata,', 'who')
('who', 'was')
('was', 'adopted')
('adopted', 'by')
('by', 'Ratanji')
('Ratanji', 'Tata,')
('Tata,', 'son')
('son', 'of')
('of', 'Jamsetji')
('Jamsetji', 'Tata,')
('Tata,', 'the')
('the', 'founder')
('founder', 'of')
('of', 'the')
('the', 'Tata')
('Tata', 'Group.')

***********   TRIGRAM    ************************
('Ratan', 'Naval', 'Tata')
('Naval', 'Tata', '(born')
('Tata', '(born', '28')
('(born', '28', 'December')
('28', 'December', '1937)')
('December', '1937)', 'is')
('1937)', 'is', 'an')
('is', 'an', 'Indian')
('an', 'Indian', 'industrialist,')
('Indian', 'industrialist,', 'philanthropist')
('industrialist,', 'philanthropist', 'and')
('philanthropist', 'and', 'former')
('and', 'former', 'chairman')
('former', 'chairman', 'of')
('chairman', 'of', 'Tata')
('of', 'Tata', 'Sons.')
('Tata', 'Sons.', 'He')
('Sons.', 'He', 'was')
('He', 'was', 'a')
('was', 'a', 'chairman')
('a', 'chairman', 'of')
('chairman', 'of', 'the')
('of', 'the', 'Tata')
('the', 'Tata', 'Group')
('Tata', 'Group', 'from')
('Group', 'from', '1990')
('from', '1990', 'to')
('1990', 'to', '2012,')
('to', '2012,', 'and')
('2012,', 'and', 'interim')
('and', 'interim', 'chairman')
('interim', 'chairman', 'from')
('chairman', 'from', 'October')
('from', 'October', '2016')
('October', '2016', 'through')
('2016', 'through', 'February')
('through', 'February', '2017.')
('February', '2017.', 'He')
('2017.', 'He', 'continues')
('He', 'continues', 'to')
('continues', 'to', 'head')
('to', 'head', 'its')
('head', 'its', 'charitable')
('its', 'charitable', 'trusts.In')
('charitable', 'trusts.In', '2008,')
('trusts.In', '2008,', 'he')
('2008,', 'he', 'received')
('he', 'received', 'the')
('received', 'the', 'Padma')
('the', 'Padma', 'Vibhushan,')
('Padma', 'Vibhushan,', 'the')
('Vibhushan,', 'the', 'second')
('the', 'second', 'highest')
('second', 'highest', 'civilian')
('highest', 'civilian', 'honour')
('civilian', 'honour', 'in')
('honour', 'in', 'India,')
('in', 'India,', 'after')
('India,', 'after', 'receiving')
('after', 'receiving', 'the')
('receiving', 'the', 'Padma')
('the', 'Padma', 'Bhushan,')
('Padma', 'Bhushan,', 'the')
('Bhushan,', 'the', 'third')
('the', 'third', 'highest')
('third', 'highest', 'civilian')
('highest', 'civilian', 'honour')
('civilian', 'honour', 'in')
('honour', 'in', '2000.He')
('in', '2000.He', 'is')
('2000.He', 'is', 'the')
('is', 'the', 'son')
('the', 'son', 'of')
('son', 'of', 'Naval')
('of', 'Naval', 'Tata,')
('Naval', 'Tata,', 'who')
('Tata,', 'who', 'was')
('who', 'was', 'adopted')
('was', 'adopted', 'by')
('adopted', 'by', 'Ratanji')
('by', 'Ratanji', 'Tata,')
('Ratanji', 'Tata,', 'son')
('Tata,', 'son', 'of')
('son', 'of', 'Jamsetji')
('of', 'Jamsetji', 'Tata,')
('Jamsetji', 'Tata,', 'the')
('Tata,', 'the', 'founder')
('the', 'founder', 'of')
('founder', 'of', 'the')
('of', 'the', 'Tata')
('the', 'Tata', 'Group.')

'''




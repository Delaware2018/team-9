#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def lang(text):
    # [START language_quickstart]
    # Imports the Google Cloud client library
    # [START language_python_migration_imports]
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    # [END language_python_migration_imports]

    # Instantiates a client
    # [START language_python_migration_client]
    client = language.LanguageServiceClient()
    # [END language_python_migration_client]

    print()

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document
    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    d = {}

    for token in tokens:
        if pos_tag[token.part_of_speech.tag] is 'NOUN' or pos_tag[token.part_of_speech.tag] is 'NUM':
            print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag],token.text.content))
            d['{}'.format(token.text.content)] = '{}'.format(pos_tag[token.part_of_speech.tag])
            print(d)
    
    if d != {}:
        print('d: ',d)

    yesrecur = 0

    if (d['month']) or ('year' in d) or ('week' in d):
        yesrecur = 1
        recur = 'Yes'
        if 'month' in d:
            interval = 'month'
        if 'year' in d:
            interval = 'year'
        if 'week' in d:
            interval = 'week'

    inv_d = {v: k for k, v in d.items()}
    don_amt = inv_d['NUM']

    print('Donation amount: ', don_amt)
    if yesrecur == 1:
        print('Recurring?: ',    recur)
        print('Interval: ',   interval)
    else:
        print('This donation does not recur.')

    #detects the sentiment of the text
    sentiment = (client.analyze_sentiment(document=document).document_sentiment)

    if sentiment.score   ==  0.0:
        print('The sentiment score is {:.1f}, therefore the sentiment is mixed.'.format(sentiment.score))
    elif sentiment.score >=  0.4:
        print('The sentiment score is {:.1f}, therefore the sentiment is positive.'.format(sentiment.score))
    elif sentiment.score <= -0.3:
        print('The sentiment score is {:.1f}, therefore the sentiment is negative.'.format(sentiment.score))
    elif sentiment.score > -0.3 and sentiment.score < 0.4:
        print('The sentiment score is {:.1f}, therefore the sentiment is neutral.'.format(sentiment.score))

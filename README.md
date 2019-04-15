# Open Data Hackathon
Code we used in **Bristol Open Data Jam/Hackathon** as well as **Pitches and commissioning session**.


# Description
## Background

Bristol City Council publishes many types of raw data to be transparent about the information they hold, and to encourage positive projects based on this data by any citizen or organisation.

One of the most recent datasets to be published by Bristol Museums is thousands of images from the British Empire and Commonwealth (BEC) collection. You can see a curated selection of these images online “Empire through the Lens”.

At a hackathon hosted by Bristol’s Open Data team with support from the Jean Golding Institute, attendees were encouraged to make use of this new dataset. Our team formed around an idea of using image style transfer, a process of transforming the artistic style of one image based on another using Convolutional Neural Networks.

In layman’s terms this method breaks down images into ‘content’ components and ‘style’ components, then combines them.


We hypothesised there would be value in restyling images from the dataset to draw out themes of Bristol’s economic and cultural history when it comes to Empire and Commonwealth.

## The team

* **Dave Rowe** – Development Technical Lead for Bristol City Council and Open Data enthusiast
* **Junfan Huang** – MSc Mathematics of Cybersecurity student in University of Bristol
* **Mark Pajak** – Head of Digital at Bristol City Council Culture Team & Bristol Museums
* **Rob Griffiths** – Bristol resident and Artificial Intelligence Consultant for BJSS in the South West
## Aim

To assess the potential of Style Transfer as a technique for bringing attention back to historical images and exploring aspects of their modern relevance.

## Method

Natalie Thurlby from the Jean Golding Institute introduced us to a method of style transfer using Lucid, a set of open source tools for working with neural networks. You can view the full Colab notebook we used here.

To start with, we hand-selected images from the collection we thought it would be interesting to transform. We tried to pair each ‘content’ image with ‘style’ images that might draw parallels with Bristol.

## Dockside Cranes
<figure>
  <img src="https://lh5.googleusercontent.com/zqknaQrOi-0f0Dsu5-ciOmBPDWDBbznHoiPvlSCgxY7_uJXKeuSEBDtYOnzqmh9pSscNF7C6qmbAvjF4MNggWOKMpReNw4UXOKkaJgcsF0OdTv0pSeRyFY6O2Oj3GqqB4dJSnJQb" alt="" title="A railway steam crane lowers a train engine onto a bogie on the dockside at Kilindini harbour, Mombasa, Kenya." />
  <figcaption></figcaption>
</figure>


When we saw this image it immediately made us think of the docks at Bristol harbourside, by the Mshed.

The SS Harmonides which transported the train [likely from Liverpool actually] to Kenya is just visible, docked further along the harbour.

In addition to the images, the data set has keywords and descriptions which provide a useful way to search and filter

[‘railway’, ‘steam’, ‘crane’, ‘lower’, ‘train’, ‘engine’, ‘bogie’, ‘dockside’, ‘Kilindini’, ‘harbour’, ‘Mombasa’, ‘Kenya’]
![](https://lh6.googleusercontent.com/si4pkz7SmXP_kU0Raw89TuT359JUb1M0-bWUcrrRUb7GEcr3eVLVw92Kc_EXv9l-m2qJ5wziPi0EMYUksjlvOtCLP2doFKBRJ-aEwWIYTm3E5doJLPIJyTOK_ajV_NZiTjL5CVSu)


We liked this painting by Mark Buck called the Cranes of Bristol Harbour. It says online that Mark studied for a degree in illustration at Bower Ashton Art College in Bristol, not too far from this place.

<figure>
  <img src="https://lh5.googleusercontent.com/CQ1ADzBLNALKQbijbnwMPp98716f8Buwte0b_A2h68waK93yDWw-V1cBTI89Pz8pRomGCiLcN7Wv8aY7gpEIf0mhK8ximA3mWob6qwKTcbBYp52pbssCvpqCEMDyJM7vMmwXfHaK" alt="" title="This image has been created as a result of adding the previous two images into the style tranfer engine." />
  <figcaption></figcaption>
</figure>


We drew an obvious parallel here between these two sets of cranes in ports around the world. The Bristol cranes are from the 1950s, but the Kenya photo was taken much earlier, in the 1920s It would be interesting to look more deeply at the cargo flows between these two ports during the 19th century.

## Cliftonwood Palace


![](https://lh5.googleusercontent.com/iyO-teEr89C69QXjTk5rFJhMlR8wSqZcVDGnOY8KflRO3An3GRyb6rmRVfc20BOoEZJF7lNHgOjdhwDSgq9hj6lbkgjHoRFNIGG8nZ0kCFsOeuhRJWv7zceMyiSUXGsuNdVbygCX)
This is a view of the Victoria Memorial, Kolkata, India in 1921.

It was commissioned by Lord Curzon to commemorate the death of Queen Victoria.
We were struck by the grandeur and formality of the photo.

Key words: [‘Victoria’, ‘Memorial’, ‘Kolkata’, ‘India’, ‘1921’] – see “topic modelling below”
<figure>
  <img src="https://lh4.googleusercontent.com/cAWJbVzHPr4it0b_Awo6oiPMTdi6HM35fYfwPSopCrs40MPG0AQbJKznKT-wknWEGZ0IXPYiFxPGFmfHltgPRZSuEM0gcb7Etz-yDOGAum9_49s1a3Nv1MEmnYWewgOkV9CXX-0A" alt="" title="A photo of the colourful Victorian terraces of Cliftonwood from the river, which have their own sense of formality." />
  <figcaption></figcaption>
</figure>
The architectural significance of these buildings in their locales and link to Queen Victoria are small parallels.

It’s funny how the system seemingly tries to reconstruct the grand building using these houses as colourful building blocks, but it ends up making it look like a shanty town.

<figure>
  <img src="https://lh3.googleusercontent.com/QmJSgpRoapai7boqkqoiayhpQGutrJmRXTD3CJvQNfajZ0u7pw-4NrWCgDVl1Esfy__xIihFsGf6QxegY2q9AZUMew4TBgUSypW_ufsi2kj6ljsqTo6VEADt3u44oXxm6fjM276n" alt="" title="This image was created by machine intelligence by taking an historical photograph and applying a style gleaned from a bristol cityscape." />
  <figcaption></figcaption>
</figure>


## Caribbean Carnival

<figure>
  <img src="https://lh3.googleusercontent.com/XfF8ouGfEL4DQKRo0Wv-EdQH4yEPEaD1bpBsJDwksxuwv2CcIj6HGQc3XdjFh3WZhzrfJlBsnusCPhjtGXjSIG-6FTPfFAgMptbBIAHu_xaE9KLm0Gd19rY_Ya49t-BzVVVQ8Emg" alt="" title="Carnival dancers on Nevis, the island in the Caribbean Sea, in 1965." />
  <figcaption></figcaption>
</figure>


Two men perform a carnival dance outdoors, accompanied by a musical band. Both dancers wear crowns adorned with peacock feathers and costumes made from ribbons and scarves.

Key words: [‘perform’, ‘carnival’, ‘dance’, ‘outdoors’, ‘accompany’, ‘musical’, ‘dancer’, ‘crown’, ‘adorn’, ‘peacock’, ‘feather’, ‘costume’, ‘ribbon’, ‘scarf’, ‘Nevis’]

<figure>
  <img src="https://lh4.googleusercontent.com/Rx2xRbDogD9TP2pWf5yCmFVqSgl0T_ckTktWlF4JdrJllpsDUZtAt-8Bj8NF20a-tOhA4HVs2hdi5aW4V90pBGaacTLioN8B7bhsX3oVznPNmPlMRuYiN4G8J-USqGJlpU9Qvbyo" alt="" title="St Pauls Carnival is an annual African-Caribbean carnival held, usually on the first Saturday of July, in St Pauls, Bristol." />
  <figcaption></figcaption>
</figure>
We selected this picture to see how the system would handle the colourful feathers and sequined outfits.

The resulting image (below) was somewhat abstract but we agreed was transformed by the vibrant colours and patterns of movement.
<figure>
  <img src="https://lh3.googleusercontent.com/VVE_7B6BaGLzW3TN2ZEhRLEYvSKIn1su05xGld_QlPSfMryS9VnofwjR7RSQzGS61-hUKXpx0sKA7ziU1TwQClIZjMmwsLhHC9ILRaTzlobtyoWkfjdBAPqSh0gRWYv4sLby0087" alt="" title="Festival colours reimagine an historical photograph using machine intelligence – but is this a valid interpretation of the past or an abstract and meaningless picture?" />
  <figcaption></figcaption>
</figure>
After generating many examples we came together to discuss some of the ethical and legal implications of this technique.

We were particularly mindful of the fact that any discussion of Empire and Commonwealth should be treated with sensitivity. For each image, it’s challenging both to appreciate fully the context and not to project novelty or inappropriate meaning onto it. 

We wondered whether this form of style transfer with heritage images was an interesting technique for people who have something to say and want an eye-catching way of communicating, but not a technique that should be used lightly – particularly with this dataset.

We often found ourselves coming back to discussions of media rights and intellectual property. None of us have a legal background but we were aware that, while we wanted to acknowledge where we had borrowed other people’s work to perform this experiment, we were generating new works of art – and it was unclear where the ownership lay.

## Service Design

We set out potential benefits of our service:

* A hosted online service to make it a more efficient process
* Advice and tips on how to calibrate and get the best results from Style Transfer
* Ability to process images in bulk
* Interactive ways of browsing the dataset
* Communication tools for publishing and sharing results
* Interfaces for public engagement with the tool – a Twitter conversational bot

On the first day we started putting together ideas for how a web service might be used to take source images from the Open Data Platform and automate the style stransfer process.

This caused us to think about potential users of the system and what debate might be sparked fromt he resulting images.

![](https://lh5.googleusercontent.com/YDCoytQdQ8z88L1Vh_ea9_ESM28IQEcpN7sHNOhaogQx2SaV5FcoMoBwCIFg6Fn1v5Rmx4LMlaVwnMNtBvPTyEiaHntwuo-AukORlA6DqQEB4B6JjaLaRoVCC_pGwUFLf36En4sQ)
## Proposition Design

A key requirement for all users would be the ability to explore and see the photographs in their original digitised form, with the available descriptions and other metadata. Those particularly interested in exploring the underlying data would appreciate having search and filter facilities that made use of fields such as location, date, and descriptions.

We would also need a simple way of choosing a set of photographs, without getting in the way of being able to continue to discover other photos. A bit like in an online shopping scenario where you add items to a basket.

The users could then choose a style to apply to their chosen photos. This would be a selection of Bristol artworks, or iconic scenes. For those wanting to apply their own style (artists, for example) we would give an option to upload their own artwork and images.

Depending on processing power, we know that such an online service could have difficulty applying style transforms in an appropriate time for people to wait. If the waiting time were over a couple of minutes it could be that the results are provided by email.

## Components
![](https://lh3.googleusercontent.com/4eKIcmF5AQVC9oyUPfd8xbfJIJtmRzv1HqVApQqkRpAfvEueR8sDTm7R0giKcPjJEaGMRfKkjda_TZJcW5zPI64XIHP2UpP80v2LAERtmoaWc0If3sOSJKknuDOoEaHWdoBaiZGD)

## Spin off products…Topic Modelling

We even successfully built a crucial component of our future service. The metadata surrounding the images includes both keywords and descriptive text. Junfan developed a script that analysed the metadata to provide a better understanding of the range of keywords that could be used to interrogate the images. This could potentially be used in the application to enable browsing by subject….

We wanted to generate a list of keywords from the long form text captions that accompanied the images. This would allow us to come up with a classification for pictures using their description. Then, users would be able to select topics and get some pictures they want.

Here in topic 2, our model has added bridge, street, river, house, gardens and some similar words into the same group.
<figure>
  <img src="http://www.labs.bristolmuseums.org.uk/wp-content/uploads/2019/03/image.png" alt="" title="Python is the language of choice for this particular application" />
  <figcaption></figcaption>
</figure>

<figure>
  <img src="http://www.labs.bristolmuseums.org.uk/wp-content/uploads/2019/03/image-2.png" alt="" title="Topic modelling reveals patterns of keyword abundance amongst the captions" />
  <figcaption></figcaption>
</figure>

<figure>
  <img src="https://lh6.googleusercontent.com/okCcflbaEUA4NegePLCRqUREqlhd4Iql4vlPHpPj3lp_Q-a6XaOWIlcX5MhM_p0vxsHzJ0ajVIjmsY2gXusP7GrirpkYndwDjy-4pjadlbNjCNcvO7ThcY6O8-LB5QxAJNv7Bdzm" alt="" title="keywords extracted from the captions can help us build an interface to allow filtering on a theme" />
  <figcaption></figcaption>
</figure>

## Reflections

After generating many examples we came together to discuss some of the ethical and legal implications of this technique.

We were particularly mindful of the fact that any discussion of Empire and Commonwealth should be treated with sensitivity. For each image, it’s challenging both to appreciate fully the context and not to project novelty or inappropriate meaning onto it. 

We wondered whether this form of style transfer with heritage images was an interesting technique for people who have something to say and want an eye-catching way of communicating, but not a technique that should be used lightly – particularly with this dataset.

We often found ourselves coming back to discussions of media rights and intellectual property. None of us have a legal background but we were aware that, while we wanted to acknowledge where we had borrowed other people’s work to perform this experiment, we were generating new works of art – and it was unclear where the ownership lay.

### Does this have potential?

We thought, on balance, yes this was an interesting technique for both artistic historians and artists interested in history.

We imagined their needs using the following user personas:
![](http://www.labs.bristolmuseums.org.uk/wp-content/uploads/2019/03/image-1.png)

* **Artistic Historians**: ‘I want to explore the stories behind these images and bring them to life in a contemporary way for my audience.’
* **Artists interested in history**: ‘I want a creative tool to provide inspiration and see what my own personal, artistic style would look like applied to heritage images’.
We spent time scoping ways we could turn our work so far into a service to support these user groups.

## References & Links

* **The repo for our application**: https://github.com/xihajun/Art-vs-History-Open-Data-Hackathon-Code
* **Open data platform**: https://opendata.bristol.gov.uk/pages/homepage/
* **Bristol Archives (British Empire and Commonwealth Collection)**: https://www.bristolmuseums.org.uk/bristol-archives/whats-at/our-collections/
## Acknowledgements

Thanks to Bristol Open for co-ordinating the Hackathon.

Thanks to Lucid contributors for developing the Style Transfer code.

Thanks to the following artists for source artwork:

Mark Buck: https://www.painters-online.co.uk/artist/markbuck

Ellie Pajak

https://www.etsy.com/shop/PapierBeau?section_id=21122286

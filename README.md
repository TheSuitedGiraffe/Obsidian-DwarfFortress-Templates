![dflegendsimport](https://github.com/user-attachments/assets/068f1f1f-c88d-42e6-869e-61be9380bbfc)

# Preparing the XML to JSON
Using CP437toUTF8.py convert your vanilla DF XML export to UTF8 as it uses CP437 by default. You'll want to rename your xml to world.xml, it just needs to be in the same folder as the python script when it runs.
After it is converted, use xmltojson.py to convert the xml to JSON.

# Preparing the Obsidian Valut
For organization, this vault is setup to have a Help Folder, a Templates Folder, a JSON folder, and World Data folder.

Imports will generate a new root folder, which can then be dragged into a different sub folder to help with organization.

# Understanding JSON
## Intro
JSON is a file format that can be used to manage large sets of data that contain various parameters, objects, and arrays.

Think of putting data in a box, then those boxes into other boxes to help organize those boxes.

## Example
Think of packing Funko POPs into a box, then I put that box into another box which can also contain another box with maybe DVDs/Blurays.

Curly brackets { } are used to denote objects, and square brackets [ ] are used to denote arrays. Arrays are lists of objects which can then have their own unique properties.

This example would look something like:


```
{
"Main Packing Box":{
	"Funko Box":[
		{
			"name": "Bob Ross",
			"theme": "Art"
			"barcode": 12345,
			"accessories":[
				{
					"name": "Raccoon"
				},
				{
					"name": "Art Easel"
				}	
			]
		},
		{
			"name": "Tracer",
			"Theme": "Overwatch",
			"barcode": 54321,
		}
	]
	"Movie Box":[
		{
			"name": "The Gate to The Minds Eye",
			"type": "DvD"
		}
		{
			"name": "The Big Lebowski"
			"type": "BluRay"
		}
	]
}
}
```


I have one main box, with 2 sub boxes in it. One box has 2 Funko Pops, one is Bob Ross, the Other is Tracer. In the other sub box is 2 movies, The Gate and The Big Lebowski.

*disclaimer*
I do not claim to be a JSON expert, but this understanding of JSON will help you understand the data that is stored with the Dwarf Fortress XML file.

# Templates
Templates are made in MarkDown(MD) format which allows for automatic formatting of notes/documents when they are imported.

The data that is imported from the JSON is handled by [HandlebarsJS](https://handlebarsjs.com/) and can be used inline with the MD format.

Referencing the previous example if I wanted to make a template I would do the following:

```
## {{name}}
This is a Funko POP of {{name}}, it from the {{theme}} theme and has a barcode value of {{barcode}}.

{{#if accessories}}
It also includes:
{{#each accessories}}
* {{this.name}}
{{/each}}
{{/if}}
```

In theory it would generate a note with this information:

# Examples
## Bob Ross
This is a FunkoPOP of Bob Ross, it is from the Art theme and has a bar code value of 12345.

It also includes:
* Raccoon
* Art Easel

---
## Tracer
This is a FunkoPOP of Tracer, it is from the Overwatch theme and has a bar code value of 54321.


# Functions
HandlebarsJS has various functions that can help import data in a more automated process. The term with-in HandlebarsJS is called [Helpers](https://handlebarsjs.com/guide/builtin-helpers.html#if).

Some of the main helpers are **if**,**each**, and **eq**.

Similar to Java, HandlebarsJS does not rely on formatting to know what is part of a function and it relies on knowing where to start and stop. Starting in generally noted by a # and ending a function is with a / .

## If
The if functions works as a way to check for conditions. For the snippet above, I check for accessories. The check starts at {{#if *list/object to check* }} and ends at the {{/if}}. This is a simple boolean check which means if it detects a object/function and will run the data that is inside the function. If the check fails it will skip it.

This is why the outputs look different for the Bob Ross and Tracer samples

## Each
The each function works like a loop and allows a sub list to be cycled through and have data extracted.

In the example above, for the accessories It starts with {{#each *list function name* }} and ends with {{/each}} which is where it stop iterating that section into the note.

The looping is to take care of multiple accessories and not just the first one. As this the data is not 1:1 it means that there could be 1 accessory, or 5. So loops resolves that guesswork.

## EQ
EQ is a way to check for a value in an If function.

It's handled as {{#if (eq object value) }}

So in my template I could write:

```
{{#if (eq name "Tracer")}}
OMG, it's TRACKER from OberWatch
{{#if}}
```

Which would only include that statement if the name value can match the String value "Tracer"

# Properties/Meta Data
Properties store metadata so it can be seen easily, and it can be used to color nodes in the graph viewer (crtl+g)

You can create properties by setting up a code snippet with 3 ``` ` ```  and doing the following

```
---
Name: {{name}}
Age: {{age}}
Sex: {{sex}}
---
```

Then when you are ready, delete the ``` ` ``` and you should be given a properties table that will auto populate.

# Final
It's also important to keep your JSON open when you're creating templates. I personall recommend using [Notepad++](https://notepad-plus-plus.org/). so you can get a general idea of the properties you're going to need to be working with.

Importing files requires the [JSON/CSV Importer](https://github.com/farling42/obsidian-import-json) community plugin for Obsidian. It can be acquired by enabling community plugins and installing it from the Community Plugin search within Obsidian.

Once installed there will be a search glass icon that appears on the left most ribbon (you can mind a shortcut to open it as well)

When you open it you'll be prompted for various settings.

### Choose JSON/CSV File
Select your Dwarf Fortress JSON file

### Choose TEMPLATE File
Select the template file you want to use.

### Field Containing the Data
This field is very important. It denotes which main array the import is going to cycle through.

So if I was importing regions, I would want to use *df_world.regions.region*, *df_world.artifacts.artifact*, etc.

### For the templates provided:
df_artifacts_TSG_012425 > df_world.artifacts.artifact

df_entities_TSG_012425 > df_world.entities.entity

df_HistoricalFigures_TSG_012425 > df_world.historical_figures.histroical_figure

df_musicalforms_TSG_012425 > df_world.musical_forms.musical_form

df_poeticforms_TSG_012425 > df_world.poetic_forms.poetic_form

df_regions_TSG_012425 > df_world.regions.region

df_sites_TSG_012425 > df_world.sites.site

df_writtencontents_TSG_012425 > df_world.written_contents.written_content


(Not Finished) df_HistoricalEvents_TSG_012525 > df_world.historical_events.historical_events


### Field to use as Note name
Allows you to use imported data to name files how they appear in the list. The data value you want to have goes inside a ${ }, you can also use multiple fields or plain text in here in addition to a data.

Make sure you use some type of import data, otherwise the importer will just overwrite on the same file over and over again.

### For the templates provided:
df_artifacts_TSG_012425 > artifact${id}

df_entities_TSG_012425 > eid${id}

df_HistoricalFigures_TSG_012425 > hfid${id}

df_musicalforms_TSG_012425 > musical_forms${id}

df_poeticforms_TSG_012425 > poetic_forms${id}

df_regions_TSG_012425 > regions${id}

df_sites_TSG_012425 > sites${id}

df_writtencontents_TSG_012425 > written_content${id}

df_HistoricalEvents_TSG_012525 > heid${id}


### How to handle existing Notes
I have this set to replace because I will import, make a change, then delete and reimport. Feel free to mess with this.

### Name of Destination Folder in Vault
This is the folder the files will be placed into. If a folder is not there, it will create a new Root folder and add the files.

I tend to delete the folder I'm working on importing items in because if there is a syntax error it will not generate a folder.

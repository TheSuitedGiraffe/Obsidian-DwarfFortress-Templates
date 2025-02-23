---
id: {{ id }}
type: {{ type }}
name: {{ name }}
coords: {{ coords }}
rectangle: {{ rectangle }}
---
# {{ name }}
* **Type:** {{ type }}
* **Coordinates:** {{ coords }}
* **Rectangle:** {{ rectangle }}
* **Site ID:** #site{{id}}
* ## Structures
{{#each structures.structure}}
	***Name:*** {{this.name}}
	 **Type:** {{this.type}}
	 **ID:** {{this.local_id}}
	{{#if structures.structure.entity_id}}
	**Entity_ID:** {{this.local_id}}
	{{/if}}
{{else}}
No structures found  for this site.
{{/each}}
# Design Document for arch template

## Processing flow

* Read architecture specs from XLSX
* Render architecture specs to JSON
* Input JSON to yogalayout for layout
* Render architecture based on computed layout

## JSON specification for layout

```json
{
    "id": "node id",
    "type": "node type",
    "margin": {"left": 1, "right": 1, "top": 1, "bottom": 1, "horizontal": 1, "vertical": 1, "all": 1},
    "padding": {"left": 1, "right": 1, "top": 1, "bottom": 1, "horizontal": 1, "vertical": 1, "all": 1},
    "flex": 1,
    "flex-direction": "row | row-reverse | column | column-reverse",
    "flex-wrap": "nowrap | wrap | wrap-reverse",
    "width": 1,
    "height": 1,
    "min-width": 1,
    "min-height": 1,
    "max-width": 1,
    "max-height": 1,
    "data": {},
    "children": [],
}
```

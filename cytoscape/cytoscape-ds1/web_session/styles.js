var styles = [ {
  "format_version" : "1.0",
  "generated_by" : "cytoscape-3.9.1",
  "target_cytoscapejs_version" : "~2.1",
  "title" : "default",
  "style" : [ {
    "selector" : "node",
    "css" : {
      "border-width" : 0.0,
      "border-opacity" : 1.0,
      "color" : "rgb(255,255,255)",
      "font-family" : "SansSerif.plain",
      "font-weight" : "normal",
      "background-opacity" : 1.0,
      "text-valign" : "center",
      "text-halign" : "center",
      "background-color" : "rgb(254,196,79)",
      "shape" : "ellipse",
      "text-opacity" : 1.0,
      "border-color" : "rgb(204,204,204)",
      "height" : 35.0,
      "font-size" : 12,
      "width" : 35.0,
      "content" : "data(name)"
    }
  }, {
    "selector" : "node[Entity_Type = 'CARDINAL']",
    "css" : {
      "background-color" : "rgb(189,189,189)"
    }
  }, {
    "selector" : "node[Entity_Type = 'WORK_OF_ART']",
    "css" : {
      "background-color" : "rgb(107,174,214)"
    }
  }, {
    "selector" : "node[Entity_Type = 'PRODUCT']",
    "css" : {
      "background-color" : "rgb(35,132,67)"
    }
  }, {
    "selector" : "node[Entity_Type = 'GPE']",
    "css" : {
      "background-color" : "rgb(251,106,74)"
    }
  }, {
    "selector" : "node[Entity_Type = 'CARDINAL']",
    "css" : {
      "shape" : "v"
    }
  }, {
    "selector" : "node[Entity_Type = 'WORK_OF_ART']",
    "css" : {
      "shape" : "octagon"
    }
  }, {
    "selector" : "node[Entity_Type = 'PERSON']",
    "css" : {
      "shape" : "roundrectangle"
    }
  }, {
    "selector" : "node[Entity_Type = 'ORG']",
    "css" : {
      "shape" : "diamond"
    }
  }, {
    "selector" : "node[Entity_Type = 'PRODUCT']",
    "css" : {
      "shape" : "octagon"
    }
  }, {
    "selector" : "node[Entity_Type = 'GPE']",
    "css" : {
      "shape" : "parallelogram"
    }
  }, {
    "selector" : "node[Degree > 1]",
    "css" : {
      "font-size" : 1
    }
  }, {
    "selector" : "node[Degree = 1]",
    "css" : {
      "font-size" : 30
    }
  }, {
    "selector" : "node[Degree > 0][Degree < 1]",
    "css" : {
      "font-size" : "mapData(Degree,0,1,10,30)"
    }
  }, {
    "selector" : "node[Degree = 0]",
    "css" : {
      "font-size" : 10
    }
  }, {
    "selector" : "node[Degree < 0]",
    "css" : {
      "font-size" : 1
    }
  }, {
    "selector" : "node:selected",
    "css" : {
      "background-color" : "rgb(255,255,0)"
    }
  }, {
    "selector" : "edge",
    "css" : {
      "target-arrow-shape" : "none",
      "line-color" : "rgb(217,217,217)",
      "font-family" : "Dialog.plain",
      "font-weight" : "normal",
      "font-size" : 10,
      "color" : "rgb(0,0,0)",
      "source-arrow-shape" : "none",
      "width" : 2.0,
      "opacity" : 1.0,
      "content" : "",
      "target-arrow-color" : "rgb(0,0,0)",
      "line-style" : "solid",
      "text-opacity" : 1.0,
      "source-arrow-color" : "rgb(0,0,0)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 41,704]",
    "css" : {
      "line-color" : "rgb(37,37,37)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness = 41,704]",
    "css" : {
      "line-color" : "rgb(68,2,86)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 20,852][EdgeBetweenness < 41,704]",
    "css" : {
      "line-color" : "mapData(EdgeBetweenness,20,852,41,704,rgb(33,145,140),rgb(68,2,86))"
    }
  }, {
    "selector" : "edge[EdgeBetweenness > 0][EdgeBetweenness < 20,852]",
    "css" : {
      "line-color" : "mapData(EdgeBetweenness,0,20,852,rgb(251,231,35),rgb(33,145,140))"
    }
  }, {
    "selector" : "edge[EdgeBetweenness = 0]",
    "css" : {
      "line-color" : "rgb(251,231,35)"
    }
  }, {
    "selector" : "edge[EdgeBetweenness < 0]",
    "css" : {
      "line-color" : "rgb(255,255,255)"
    }
  }, {
    "selector" : "edge:selected",
    "css" : {
      "line-color" : "rgb(255,0,0)"
    }
  } ]
} ]
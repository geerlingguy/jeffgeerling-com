---
nid: 2460
title: "Multi-value spatial search with Solr 4.x and Drupal 7"
slug: "multi-value-spatial-search"
date: 2014-07-11T19:59:34+00:00
drupal:
  nid: 2460
  path: /blogs/jeff-geerling/multi-value-spatial-search
  body_format: full_html
  redirects: []
tags:
  - drupal
  - drupal 7
  - drupal planet
  - location
  - schema
  - solr
  - spatial
---

<p>For some time, Solr 3.x and Drupal 7 have been able to do geospatial search (using the location module, geofield, or other modules that stored latitude and longitude coordinates in Drupal that could be indexed by Apache Solr). Life was good—as long as you only had one location per node!</p>

<p>Sometimes, you may have a node (say a product, or a personality) affiliated with multiple locations. Perhaps you have a hammer that's available in three of your company's stores, or a speaker who is available to speak in two locations. When solr 3.x and Drupal 7 encountered this situation, you would either use a single location value in the index (so the second, third, etc. fields weren't indexed or searched), or if you put multiple values into solr's search index using the <code>LatLonType</code>, solr could throw out unexpected results (sometimes combining the closest latitude and closest longitude to a given point, meaning you get strange search results).</p>

<p>With Solr 4.x, especially Solr 4.3 and 4.5, there were some great improvements to spatial search, mostly enabled by switching from the old and trusty single-value <code>LatLonType</code> to the new (but slightly slower) <a href="https://cwiki.apache.org/confluence/display/solr/Spatial+Search#SpatialSearch-SpatialRecursivePrefixTreeFieldType(abbreviatedasRPT"><code>SpatialRecursivePrefixTreeFieldType</code></a>, or RPT for short.</p>

<p>Enabling this field type for the multi-value location field used by Apache Solr Search Integration and Search API involves an addition and a change in your schema.xml file. First, add the following after the "location" fieldType definition:</p>


```
<fieldType name="location_rpt" class="solr.SpatialRecursivePrefixTreeFieldType"
           distErrPct="0.025"
           maxDistErr="0.000009"
           units="degrees" />
```

<p>Then, find the <code>locm_*</code> dynamicField definition later in the file, and update it to use the new <code>location_rpt</code> fieldType we just defined:</p>


```
<dynamicField name="locm_*" type="location_rpt" indexed="true"  stored="true" multiValued="true"/>
```

<p>Once this is done, you will need to reindex your site (or at least all the content with location/geo fields). Once that's done, your search results can use a location filter (perhaps a user's entered or detected location), and that filter will apply to <em>all</em> the values attached to a particular node.</p>

<p>Some other advantages offered by the RPT field type (as opposed to the LatLonType) include:</p>

<ul>
<li>Query by polygons and other complex shapes, in addition to circles &amp; rectangles</li>
<li>Multi-valued indexed fields</li>
<li>Ability to index non-point shapes (e.g. polygons) as well as point shapes</li>
<li>Rectangles with user-specified corners that can cross the dateline</li>
<li>Multi-value distance sort and score boosting (warning: non-optimized)</li>
<li>Well-Known-Text (WKT) shape syntax (required for specifying polygons &amp; other complex shapes)</li>
</ul>

<p>Some of these features (<em>not</em> including the multi-value support) also require the addition of the property <code>spatialContextFactory="com.spatial4j.core.context.jts.JtsSpatialContextFactory"</code> to the <code>fieldType</code> definition in schema.xml as well as the installation of the <a href="http://sourceforge.net/projects/jts-topo-suite/">JTS</a> library to your Solr class path.</p>

<p>See more in the Apache Solr docs: <a href="https://cwiki.apache.org/confluence/display/solr/Spatial+Search#SpatialSearch-SpatialRecursivePrefixTreeFieldType(abbreviatedasRPT)">SpatialRecursivePrefixTreeFieldType (abbreviated as RPT)</a>. Also, check out this issue proposing we add the above configuration (and updated documentation) to the shared configuration for Apache Solr/Search API: <a href="https://www.drupal.org/node/2038133#comment-8960451">Spatial search improvements - new spatial fieldType on Solr 4</a>.</p>

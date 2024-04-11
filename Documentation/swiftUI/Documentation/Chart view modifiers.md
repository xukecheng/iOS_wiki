Instance Method

# chartBackground(alignment:content:)

Adds a background to a view that contains a chart.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartBackground<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: @escaping (ChartProxy) -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment of the content.

`content`

    

The content of the background.

## Discussion

You can use this modifier to define a background view as a function of the
chart in the view. You can access the chart with the `ChartProxy` object
passed into the closure.

Note

If `self` contains more than one chart, the chart proxy will refer to the
first chart.

## See Also

### Styles

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(_:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<DataValue, S>(_ mapping: KeyValuePairs<DataValue, S>) -> some View where DataValue : Plottable, S : ShapeStyle
    

##  Parameters

`mapping`

    

Maps data categories to foreground styles.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(domain:range:type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ShapeStyle
    

##  Parameters

`domain`

    

The possible data values plotted as foreground style in the chart. You can
define the domain with a `ClosedRange` for number or `Date` values (e.g., `0
... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of foreground styles that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(domain:type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as foreground style in the chart. You can
define the domain with a `ClosedRange` for number or `Date` values (e.g., `0
... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(domain:mapping:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Domain, S>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> S
    ) -> some View where Domain : Collection, S : ShapeStyle, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as foreground style in the chart.

`mapping`

    

Maps data categories to foreground styles.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(mapping:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<DataValue, S>(mapping: @escaping (DataValue) -> S) -> some View where DataValue : Plottable, S : ShapeStyle
    

##  Parameters

`mapping`

    

Maps data categories to foreground styles.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(range:type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : ScaleRange, Range.VisualValue : ShapeStyle
    

##  Parameters

`range`

    

The range of foreground styles that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartForegroundStyleScale(type:)

Configures the foreground style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartForegroundStyleScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some
View`

Configures the plot area of charts.

Instance Method

# chartPlotStyle(content:)

Configures the plot area of charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartPlotStyle<Content>(@ViewBuilder content: @escaping (ChartPlotContent) -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A closure that returns the content of the plot area.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of
charts.

For example:

## See Also

### Styles

`func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) ->
some View`

Adds a background to a view that contains a chart.

`func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range,
type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping:
(Domain.Element) -> S) -> some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) ->
some View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the foreground style scale for charts.

`func chartForegroundStyleScale(type: ScaleType?) -> some View`

Configures the foreground style scale for charts.

Instance Method

# chartLegend(_:)

Configures the legend for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLegend(_ visibility: Visibility) -> some View
    

##  Parameters

`visibility`

    

The visibility of the legend.

## See Also

### Legends

`func chartLegend(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?) -> some View`

Configures the legend for charts.

`func chartLegend<Content>(position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?, content: () -> Content) -> some View`

Configures the legend for charts.

Instance Method

# chartLegend(position:alignment:spacing:)

Configures the legend for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLegend(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View
    

##  Parameters

`position`

    

Configures the position of the legend.

`alignment`

    

Alignment of the legend within the space available to it. Use `nil` for
default alignment.

`spacing`

    

Distance between the legend and the chart. Use `nil` for the default spacing.

## See Also

### Legends

`func chartLegend(Visibility) -> some View`

Configures the legend for charts.

`func chartLegend<Content>(position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?, content: () -> Content) -> some View`

Configures the legend for charts.

Instance Method

# chartLegend(position:alignment:spacing:content:)

Configures the legend for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLegend<Content>(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> Content
    ) -> some View where Content : View
    

##  Parameters

`position`

    

Configures the position of the legend.

`alignment`

    

Alignment of the legend within the space available to it. Use `nil` for
default alignment.

`spacing`

    

Distance between the legend and the chart. Use `nil` for the default spacing.

`content`

    

The content of the legend.

## See Also

### Legends

`func chartLegend(Visibility) -> some View`

Configures the legend for charts.

`func chartLegend(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?) -> some View`

Configures the legend for charts.

Instance Method

# chartOverlay(alignment:content:)

Adds an overlay to a view that contains a chart.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartOverlay<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: @escaping (ChartProxy) -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment of the content.

`content`

    

The content of the overlay.

## Discussion

You can use this modifier to define an overlay view as a function of the chart
in the view. You can access the chart with the `ChartProxy` object passed into
the closure.

Below is an example where we define an overlay view that handles drag gestures
and use the proxy to convert the gesture coordinates to data values in the
chart.

Note

If `self` contains more than one chart, the chart proxy will refer to the
first chart.

Instance Method

# chartXAxis(_:)

Sets the visibility of the x axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxis(_ visibility: Visibility) -> some View
    

## See Also

### Axes

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartXAxis(content:)

Configures the x-axis for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent
    

##  Parameters

`content`

    

The axis content.

## Discussion

Use this modifier to customize the x-axis of a chart. Provide an `AxisMarks`
builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel`
structures to form the axis. Omit components from the builder to omit them
from the resulting axis. For example, the following code adds grid lines to
the x-axis:

You can also compose multiple `AxisMarks` to create more complex axes:

The above example above customizes the x-axis using two `AxisMarks`
declarations. The first creates a grid line for every hour in the day. The
second adds a tick and label for every six hours in the day, with a second
line showing the date for the very beginning of the axis.

Note

To add an axis label, use one of the label modifiers, like
`chartXAxisLabel(position:alignment:spacing:content:)`.

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartXAxisStyle(content:)

Configures the x axis content of charts.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A closure that returns the content of the axis.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of
charts.

For example:

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartYAxis(_:)

Sets the visibility of the y axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxis(_ visibility: Visibility) -> some View
    

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartYAxis(content:)

Configures the y-axis for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent
    

##  Parameters

`content`

    

The axis content.

## Discussion

Use this modifier to customize the y-axis of a chart. Provide an `AxisMarks`
builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel`
structures to form the axis. Omit components from the builder to omit them
from the resulting axis. For example, the following code adds grid lines to
the y-axis:

Use arguments such as `position:` or `values:` to control the placement of the
axis values it displays.

The above code customizes the y-axis to appear on the leading edge of the
chart, with a solid grid line at the 0% and 100% marks.

Note

To add an axis label, use one of the label modifiers, like
`chartYAxisLabel(position:alignment:spacing:content:)`.

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the y axis content of charts.

Instance Method

# chartYAxisStyle(content:)

Configures the y axis content of charts.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View
    

##  Parameters

`content`

    

A closure that returns the content of the axis.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of
charts.

For example:

## See Also

### Axes

`func chartXAxis(Visibility) -> some View`

Sets the visibility of the x axis.

`func chartXAxis<Content>(content: () -> Content) -> some View`

Configures the x-axis for charts in the view.

`func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some
View`

Configures the x axis content of charts.

`func chartYAxis(Visibility) -> some View`

Sets the visibility of the y axis.

`func chartYAxis<Content>(content: () -> Content) -> some View`

Configures the y-axis for charts in the view.

Instance Method

# chartXAxisLabel(_:position:alignment:spacing:)

Adds x axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxisLabel<S>(
        _ label: S,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View where S : StringProtocol
    

##  Parameters

`title`

    

The label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartXAxisLabel(_:position:alignment:spacing:)

Adds x axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxisLabel(
        _ labelKey: LocalizedStringKey,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View
    

##  Parameters

`labelKey`

    

The key for the localized label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartXAxisLabel(position:alignment:spacing:content:)

Adds x axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXAxisLabel<C>(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> C
    ) -> some View where C : View
    

##  Parameters

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

`content`

    

The label content.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartYAxisLabel(_:position:alignment:spacing:)

Adds y axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxisLabel<S>(
        _ label: S,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

The label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartYAxisLabel(_:position:alignment:spacing:)

Adds y axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxisLabel(
        _ labelKey: LocalizedStringKey,
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil
    ) -> some View
    

##  Parameters

`labelKey`

    

The key for the localized label string.

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartYAxisLabel(position:alignment:spacing:content:)

Adds y axis label for charts in the view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYAxisLabel<C>(
        position: AnnotationPosition = .automatic,
        alignment: Alignment? = nil,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> C
    ) -> some View where C : View
    

##  Parameters

`position`

    

The position of the label.

`alignment`

    

The alignment of the label.

`spacing`

    

The spacing of the label from the axis markers.

`content`

    

The label content.

## See Also

### Axis Labels

`func chartXAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds x axis label for charts in the view.

`func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?,
spacing: CGFloat?, content: () -> C) -> some View`

Adds x axis label for charts in the view.

`func chartYAxisLabel<S>(S, position: AnnotationPosition, alignment:
Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

`func chartYAxisLabel(LocalizedStringKey, position: AnnotationPosition,
alignment: Alignment?, spacing: CGFloat?) -> some View`

Adds y axis label for charts in the view.

Instance Method

# chartXScale(domain:range:type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
    

##  Parameters

`domain`

    

The possible data values along the x axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of x positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartXScale(domain:type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values along the x axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartXScale(range:type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : PositionScaleRange
    

##  Parameters

`range`

    

The range of x positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartXScale(type:)

Configures the x scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartXScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(domain:range:type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
    

##  Parameters

`domain`

    

The possible data values along the y axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of y positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(domain:type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values along the y axis in the chart. You can define the
domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`),
and with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(range:type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : PositionScaleRange
    

##  Parameters

`range`

    

The range of y positions that correspond to the scale domain. By default the
range is determined by the dimension of the plot area. You can use `range:
.plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale(type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartYScale(type:)

Configures the y scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartYScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Axis scales

`func chartXScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartXScale(type: ScaleType?) -> some View`

Configures the x scale for charts.

`func chartYScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View`

Configures the y scale for charts.

`func chartYScale<Range>(range: Range, type: ScaleType?) -> some View`

Configures the y scale for charts.

Instance Method

# chartSymbolScale(_:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<DataValue, S>(_ mapping: KeyValuePairs<DataValue, S>) -> some View where DataValue : Plottable, S : ChartSymbolShape
    

##  Parameters

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(_:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<DataValue>(_ mapping: KeyValuePairs<DataValue, any ChartSymbolShape>) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain>(domain: Domain) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as symbols in the chart. You can define the
domain with an array for categorical values (e.g., `["A", "B", "C"]`)

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain, Range>(
        domain: Domain,
        range: Range
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ChartSymbolShape
    

##  Parameters

`domain`

    

The possible data values plotted as symbols in the chart. You can define the
domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain>(
        domain: Domain,
        range: [any ChartSymbolShape]
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as symbols in the chart. You can define the
domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(domain:mapping:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Domain, S>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> S
    ) -> some View where Domain : Collection, S : ChartSymbolShape, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as symbol in the chart.

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(mapping:)

Configures the symbol scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<DataValue, S>(mapping: @escaping (DataValue) -> S) -> some View where DataValue : Plottable, S : ChartSymbolShape
    

##  Parameters

`mapping`

    

Maps data categories to symbol shapes.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale(range: [any ChartSymbolShape]) -> some View
    

##  Parameters

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Range>(range: Range) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolScale(range:)

Configures the symbol style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolScale<Range>(range: Range) -> some View where Range : ScaleRange, Range.VisualValue : ChartSymbolShape
    

##  Parameters

`range`

    

The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

`func chartSymbolScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some
View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue>(KeyValuePairs<DataValue, any
ChartSymbolShape>) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<Domain>(domain: Domain) -> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain>(domain: Domain, range: [any ChartSymbolShape])
-> some View`

Configures the symbol style scale for charts.

`func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) ->
S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View`

Configures the symbol scale for charts.

`func chartSymbolScale(range: [any ChartSymbolShape]) -> some View`

Configures the symbol style scale for charts.

Instance Method

# chartSymbolSizeScale(_:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<DataValue>(_ mapping: KeyValuePairs<DataValue, CGFloat>) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to symbol sizes.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(domain:range:type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Domain, Range>(
        domain: Domain,
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue == CGFloat
    

##  Parameters

`domain`

    

The possible data values plotted as symbol sizes in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of symbol size that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(domain:type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Domain>(
        domain: Domain,
        type: ScaleType? = nil
    ) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as symbol sizes in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(domain:mapping:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Domain>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> CGFloat
    ) -> some View where Domain : Collection, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as symbol size in the chart.

`mapping`

    

Maps data categories to symbol sizes.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(mapping:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<DataValue>(mapping: @escaping (DataValue) -> CGFloat) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to symbol sizes.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(range:type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale<Range>(
        range: Range,
        type: ScaleType? = nil
    ) -> some View where Range : ScaleRange, Range.VisualValue == CGFloat
    

##  Parameters

`range`

    

The range of symbol size that correspond to the scale domain.

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale(type: ScaleType?) -> some View`

Configures the symbol size scale for charts.

Instance Method

# chartSymbolSizeScale(type:)

Configures the symbol size scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartSymbolSizeScale(type: ScaleType? = nil) -> some View
    

##  Parameters

`type`

    

The scale type.

## See Also

### Symbol size scales

`func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) ->
some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type:
ScaleType?) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element)
-> CGFloat) -> some View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some
View`

Configures the symbol size scale for charts.

`func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some
View`

Configures the symbol size scale for charts.

Instance Method

# chartLineStyleScale(_:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<DataValue>(_ mapping: KeyValuePairs<DataValue, StrokeStyle>) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to line styles.

## See Also

### Line style scales

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(domain:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Domain>(domain: Domain) -> some View where Domain : ScaleDomain
    

##  Parameters

`domain`

    

The possible data values plotted as line styles in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(domain:range:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Domain, Range>(
        domain: Domain,
        range: Range
    ) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue == StrokeStyle
    

##  Parameters

`domain`

    

The possible data values plotted as line styles in the chart. You can define
the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

`range`

    

The range of line styles that correspond to the scale domain.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(range:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Range>(range: Range) -> some View where Range : ScaleRange, Range.VisualValue == StrokeStyle
    

##  Parameters

`range`

    

The range of line styles that correspond to the scale domain.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(domain:mapping:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<Domain>(
        domain: Domain,
        mapping: @escaping (Domain.Element) -> StrokeStyle
    ) -> some View where Domain : Collection, Domain.Element : Plottable
    

##  Parameters

`domain`

    

The possible data values plotted as line style in the chart.

`mapping`

    

Maps data categories to line styles.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) ->
some View`

Configures the line style scale for charts.

Instance Method

# chartLineStyleScale(mapping:)

Configures the line style scale for charts.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func chartLineStyleScale<DataValue>(mapping: @escaping (DataValue) -> StrokeStyle) -> some View where DataValue : Plottable
    

##  Parameters

`mapping`

    

Maps data categories to line styles.

## See Also

### Line style scales

`func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) ->
some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some
View`

Configures the line style scale for charts.

`func chartLineStyleScale<Range>(range: Range) -> some View`

Configures the line style scale for charts.

`func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) ->
StrokeStyle) -> some View`

Configures the line style scale for charts.

Instance Method

# chartScrollPosition(initialX:)

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(initialX: some Plottable) -> some View
    

##  Parameters

`initialValue`

    

The initial scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollPosition(initialY:)

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(initialY: some Plottable) -> some View
    

##  Parameters

`initialValue`

    

The initial scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollPosition(x:)

Associates a binding to be updated when the chart scrolls along the x-axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(x: Binding<some Plottable>) -> some View
    

##  Parameters

`value`

    

The scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollPosition(y:)

Associates a binding to be updated when the chart scrolls along the y-axis.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollPosition(y: Binding<some Plottable>) -> some View
    

##  Parameters

`value`

    

The scroll position as a value.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollTargetBehavior(_:)

Sets the scroll behavior of the scrollable chart.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollTargetBehavior(_ behavior: some ChartScrollTargetBehavior) -> some View
    

##  Parameters

`behavior`

    

The chart scroll target behavior.

## Discussion

Use this method to control how the chart scrolls and aligns when the user
finishes scrolling. The example below sets the scroll target behavior to align
to the values in the chart. When the user finishes scrolling, the chart will
settle to align with the values in the chart.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollableAxes(Axis.Set) -> some View`

Configures the scrollable behavior of charts in this view.

Instance Method

# chartScrollableAxes(_:)

Configures the scrollable behavior of charts in this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartScrollableAxes(_ axes: Axis.Set) -> some View
    

##  Parameters

`axes`

    

The set of axes to enable scrolling.

## Discussion

Use this method to make a chart scrollable. Below is an example that makes a
chart scrollable along the horizontal axis.

Note

When scrolling is enabled along an axis, a default portion of the chart will
be made visible. You can use the `chartXVisibleDomain` or
`chartYVisibleDomain` modifiers to configure the visible domain.

## See Also

### Scrolling

`func chartScrollPosition(initialX: some Plottable) -> some View`

Sets the initial scroll position along the x-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(initialY: some Plottable) -> some View`

Sets the initial scroll position along the y-axis. Once the user scrolls the
scroll view, the value provided to this modifier will have no effect.

`func chartScrollPosition(x: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the x-axis.

`func chartScrollPosition(y: Binding<some Plottable>) -> some View`

Associates a binding to be updated when the chart scrolls along the y-axis.

`func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View`

Sets the scroll behavior of the scrollable chart.

Instance Method

# chartXSelection(range:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View where P : Plottable, P : Comparable
    

## See Also

### Selection

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartXSelection(value:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXSelection<P>(value: Binding<P?>) -> some View where P : Plottable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartYSelection(range:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View where P : Plottable, P : Comparable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartYSelection(value:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYSelection<P>(value: Binding<P?>) -> some View where P : Plottable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartAngleSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartAngleSelection(value:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartAngleSelection<P>(value: Binding<P?>) -> some View where P : Plottable
    

## See Also

### Selection

`func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartXSelection<P>(value: Binding<P?>) -> some View`

`func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View`

`func chartYSelection<P>(value: Binding<P?>) -> some View`

Instance Method

# chartXVisibleDomain(length:)

Sets the length of the visible domain in the X dimension.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartXVisibleDomain<P>(length: P) -> some View where P : Plottable, P : Numeric
    

##  Parameters

`length`

    

The length of the visible domain measured in data units. For categorical data,
this should be the number of visible categories.

## Discussion

Use this method to control how much of the chart is visible in a scrollable
chart. The example below sets the visible portion of the chart to 10 units in
the X axis.

## See Also

### Visible domain

`func chartYVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the Y dimension.

Instance Method

# chartYVisibleDomain(length:)

Sets the length of the visible domain in the Y dimension.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartYVisibleDomain<P>(length: P) -> some View where P : Plottable, P : Numeric
    

##  Parameters

`length`

    

The length of the visible domain measured in data units. For categorical data,
this should be the number of visible categories.

## Discussion

Use this method to control how much of the chart is visible in a scrollable
chart. The example below sets the visible portion of the chart to 10 units in
the Y axis.

## See Also

### Visible domain

`func chartXVisibleDomain<P>(length: P) -> some View`

Sets the length of the visible domain in the X dimension.

Instance Method

# chartGesture(_:)

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func chartGesture(_ gesture: @escaping (ChartProxy) -> some Gesture) -> some View
    


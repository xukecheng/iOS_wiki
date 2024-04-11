Instance Method

# font(_:)

Sets the default font for text in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func font(_ font: Font?) -> some View
    

##  Parameters

`font`

    

The default font to use in this view.

## Return Value

A view with the default font set to the value you supply.

## Discussion

Use `font(_:)` to apply a specific font to all of the text in a view.

The example below shows the effects of applying fonts to individual views and
to view hierarchies. Font information flows down the view hierarchy as part of
the environment, and remains in effect unless overridden at the level of an
individual view or view container.

Here, the outermost `VStack` applies a 16-point system font as a default font
to views contained in that `VStack`. Inside that stack, the example applies a
`largeTitle` font to just the first text view; this explicitly overrides the
default. The remaining stack and the views contained with it continue to use
the 16-point system font set by their containing view:

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# dynamicTypeSize(_:)

Sets the Dynamic Type size within the view to the given value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func dynamicTypeSize(_ size: DynamicTypeSize) -> some View
    

##  Parameters

`size`

    

The size to set for this view.

## Return Value

A view that sets the Dynamic Type size to the specified `size`.

## Discussion

As an example, you can set a Dynamic Type size in `ContentView` to be
`DynamicTypeSize.xLarge` (this can be useful in previews to see your content
at a different size) like this:

If a Dynamic Type size range is applied after setting a value, the value is
limited by that range:

When limiting the Dynamic Type size, consider if adding a large content view
with `accessibilityShowsLargeContentViewer()` would be appropriate.

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Method

# dynamicTypeSize(_:)

Limits the Dynamic Type size within the view to the given range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func dynamicTypeSize<T>(_ range: T) -> some View where T : RangeExpression, T.Bound == DynamicTypeSize
    

##  Parameters

`range`

    

The range of sizes that are allowed in this view.

## Return Value

A view that constrains the Dynamic Type size of this view within the specified
`range`.

## Discussion

As an example, you can constrain the maximum Dynamic Type size in
`ContentView` to be no larger than `DynamicTypeSize.large`:

If the Dynamic Type size is limited to multiple ranges, the result is their
intersection:

A specific Dynamic Type size can still be set after a range is applied:

When limiting the Dynamic Type size, consider if adding a large content view
with `accessibilityShowsLargeContentViewer()` would be appropriate.

## See Also

### Adjusting text size

`func textScale(Text.Scale, isEnabled: Bool) -> some View`

Applies a text scale to text in the view.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Method

# bold(_:)

Applies a bold font weight to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func bold(_ isActive: Bool = true) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether bold font styling is added. The default
value is `true`.

## Return Value

A view with bold text.

## See Also

### Controlling text style

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# fontDesign(_:)

Sets the font design of the text in this view.

iOS 16.1+  iPadOS 16.1+  macOS 13.0+  Mac Catalyst 16.1+  tvOS 16.1+  watchOS
9.1+  visionOS 1.0+

    
    
    func fontDesign(_ design: Font.Design?) -> some View
    

##  Parameters

`design`

    

One of the available font designs. Providing `nil` removes the effect of any
font design modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font design you specify.

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# fontWeight(_:)

Sets the font weight of the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func fontWeight(_ weight: Font.Weight?) -> some View
    

##  Parameters

`weight`

    

One of the available font weights. Providing `nil` removes the effect of any
font weight modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font weight you specify.

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWidth(Font.Width?) -> some View`

Sets the font width of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# fontWidth(_:)

Sets the font width of the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func fontWidth(_ width: Font.Width?) -> some View
    

##  Parameters

`width`

    

One of the available font widths. Providing `nil` removes the effect of any
font width modifier applied higher in the view hierarchy.

## Return Value

A view that uses the font width you specify.

## See Also

### Setting a font

Applying custom fonts to text

Add and use a font in your app that scales with Dynamic Type.

`func font(Font?) -> some View`

Sets the default font for text in this view.

`func fontDesign(Font.Design?) -> some View`

Sets the font design of the text in this view.

`func fontWeight(Font.Weight?) -> some View`

Sets the font weight of the text in this view.

`var font: Font?`

The default font of this environment.

`struct Font`

An environment-dependent font.

Instance Method

# italic(_:)

Applies italics to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func italic(_ isActive: Bool = true) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether italic styling is added. The default
value is `true`.

## Return Value

A View with italic text.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# monospaced(_:)

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func monospaced(_ isActive: Bool = true) -> some View
    

## Return Value

A view whose child views’ fonts use fixed-width characters, while leaving
other characters proportionally spaced.

## Discussion

If a child view’s base font doesn’t support fixed-width, the font remains
unchanged.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# monospacedDigit()

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func monospacedDigit() -> some View
    

## Return Value

A view whose child views’ fonts use fixed-width numeric characters, while
leaving other characters proportionally spaced.

## Discussion

Using fixed-width digits allows you to easily align numbers of the same size
in a table-like arrangement. This feature is also known as “tabular figures”
or “tabular numbers.”

This modifier only affects numeric characters, and leaves all other characters
unchanged.

The following example shows the effect of `monospacedDigit()` on multiple
child views. The example consists of two `VStack` views inside an `HStack`.
Each `VStack` contains two `Button` views, with the second `VStack` applying
the `monospacedDigit()` modifier to its contents. As a result, the digits in
the buttons in the trailing `VStack` are the same width, which in turn gives
the buttons equal widths.

If a child view’s base font doesn’t support fixed-width digits, the font
remains unchanged.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

Instance Method

# strikethrough(_:pattern:color:)

Applies a strikethrough to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func strikethrough(
        _ isActive: Bool = true,
        pattern: Text.LineStyle.Pattern = .solid,
        color: Color? = nil
    ) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether strikethrough is added. The default
value is `true`.

`pattern`

    

The pattern of the line. The default value is `solid`.

`color`

    

The color of the strikethrough. If `color` is `nil`, the strikethrough uses
the default foreground color.

## Return Value

A view where text has a line through its center.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# textCase(_:)

Sets a transform for the case of the text contained in this view when
displayed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func textCase(_ textCase: Text.Case?) -> some View
    

##  Parameters

`textCase`

    

One of the `Text.Case` enumerations; the default is `nil`.

## Return Value

A view that transforms the case of the text.

## Discussion

The default value is `nil`, displaying the text without any case changes.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> some
View`

Applies an underline to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# textScale(_:isEnabled:)

Applies a text scale to text in the view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func textScale(
        _ scale: Text.Scale,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`scale`

    

The text scale to apply.

`isEnabled`

    

If true the text scale is applied; otherwise text scale is unchanged.

## Return Value

A view with the specified text scale applied.

## See Also

### Adjusting text size

`func dynamicTypeSize<T>(T) -> some View`

Limits the Dynamic Type size within the view to the given range.

`func dynamicTypeSize(DynamicTypeSize) -> some View`

Sets the Dynamic Type size within the view to the given value.

`var dynamicTypeSize: DynamicTypeSize`

The current Dynamic Type size.

`enum DynamicTypeSize`

A Dynamic Type size, which specifies how large scalable content should be.

`struct ScaledMetric`

A dynamic property that scales a numeric value.

Instance Method

# underline(_:pattern:color:)

Applies an underline to the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func underline(
        _ isActive: Bool = true,
        pattern: Text.LineStyle.Pattern = .solid,
        color: Color? = nil
    ) -> some View
    

##  Parameters

`isActive`

    

A Boolean value that indicates whether underline is added. The default value
is `true`.

`pattern`

    

The pattern of the line. The default value is `solid`.

`color`

    

The color of the underline. If `color` is `nil`, the underline uses the
default foreground color.

## Return Value

A view where text has a line running along its baseline.

## See Also

### Controlling text style

`func bold(Bool) -> some View`

Applies a bold font weight to the text in this view.

`func italic(Bool) -> some View`

Applies italics to the text in this view.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
some View`

Applies a strikethrough to the text in this view.

`func textCase(Text.Case?) -> some View`

Sets a transform for the case of the text contained in this view when
displayed.

`var textCase: Text.Case?`

A stylistic override to transform the case of `Text` when displayed, using the
environment’s locale.

`func monospaced(Bool) -> some View`

Modifies the fonts of all child views to use the fixed-width variant of the
current font, if possible.

`func monospacedDigit() -> some View`

Modifies the fonts of all child views to use fixed-width digits, if possible,
while leaving other characters proportionally spaced.

Instance Method

# allowsTightening(_:)

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func allowsTightening(_ flag: Bool) -> some View
    

##  Parameters

`flag`

    

A Boolean value that indicates whether the space between characters compresses
when necessary.

## Return Value

A view that can compress the space between characters when necessary to fit
text in a line.

## Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character
spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects
of `allowsTightening(_:)` on the compression of the spacing between
characters:

## See Also

### Controlling hit testing

`func contentShape<S>(S, eoFill: Bool) -> some View`

Defines the content shape for hit testing.

`func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View`

Sets the content shape for this view.

`struct ContentShapeKinds`

A kind for the content shape of a view.

Instance Method

# baselineOffset(_:)

Sets the vertical offset for the text relative to its baseline in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func baselineOffset(_ baselineOffset: CGFloat) -> some View
    

##  Parameters

`baselineOffset`

    

The amount to shift the text vertically (up or down) relative to its baseline.

## Return Value

A view where text is above or below its baseline.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# flipsForRightToLeftLayoutDirection(_:)

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func flipsForRightToLeftLayoutDirection(_ enabled: Bool) -> some View
    

##  Parameters

`enabled`

    

A Boolean value that indicates whether this view should have its content
flipped horizontally when the layout direction is right-to-left. By default,
views will adjust their layouts automatically in a right-to-left context and
do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally when the layout
direction is right-to-left.

## Discussion

Use `flipsForRightToLeftLayoutDirection(_:)` when you need the system to
horizontally mirror the contents of the view when presented in a right-to-left
layout.

To override the layout direction for a specific view, use the
`environment(_:_:)` view modifier to explicitly override the `layoutDirection`
environment value for the view.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# kerning(_:)

Sets the spacing, or kerning, between characters for the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func kerning(_ kerning: CGFloat) -> some View
    

##  Parameters

`kerning`

    

The spacing to use between individual characters in text. Value of `0` sets
the kerning to the system default value.

## Return Value

A view where text has the specified amount of kerning.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# minimumScaleFactor(_:)

Sets the minimum amount that text in this view scales down to fit in the
available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func minimumScaleFactor(_ factor: CGFloat) -> some View
    

##  Parameters

`factor`

    

A fraction between 0 and 1 (inclusive) you use to specify the minimum amount
of text scaling that this view permits.

## Return Value

A view that limits the amount of text downscaling.

## Discussion

Use the `minimumScaleFactor(_:)` modifier if the text you place in a view
doesn’t fit and it’s okay if the text shrinks to accommodate. For example, a
label with a minimum scale factor of `0.5` draws its text in a font size as
small as half of the actual font if needed.

In the example below, the `HStack` contains a `Text` label with a line limit
of `1`, that is next to a `TextField`. To allow the label to fit into the
available space, the `minimumScaleFactor(_:)` modifier shrinks the text as
needed to fit into the available space.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# tracking(_:)

Sets the tracking for the text in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func tracking(_ tracking: CGFloat) -> some View
    

##  Parameters

`tracking`

    

The amount of additional space, in points, that the view should add to each
character cluster after layout. Value of `0` sets the tracking to the system
default value.

## Return Value

A view where text has the specified amount of tracking.

## See Also

### Managing text layout

`func truncationMode(Text.TruncationMode) -> some View`

Sets the truncation mode for lines of text that are too long to fit in the
available space.

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# truncationMode(_:)

Sets the truncation mode for lines of text that are too long to fit in the
available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func truncationMode(_ mode: Text.TruncationMode) -> some View
    

##  Parameters

`mode`

    

The truncation mode that specifies where to truncate the text within the text
view, if needed. You can truncate at the beginning, middle, or end of the text
view.

## Return Value

A view that truncates text at different points in a line depending on the mode
you select.

## Discussion

Use the `truncationMode(_:)` modifier to determine whether text in a long line
is truncated at the beginning, middle, or end. Truncation is indicated by
adding an ellipsis (…) to the line when removing text to indicate to readers
that text is missing.

In the example below, the bounds of text view constrains the amount of text
that the view displays and the `truncationMode(_:)` specifies from which
direction and where to display the truncation indicator:

## See Also

### Managing text layout

`var truncationMode: Text.TruncationMode`

A value that indicates how the layout truncates the last line of text to fit
into the available space.

`func allowsTightening(Bool) -> some View`

Sets whether text in this view can compress the space between characters when
necessary to fit text in a line.

`var allowsTightening: Bool`

A Boolean value that indicates whether inter-character spacing should tighten
to fit the text into the available space.

`func minimumScaleFactor(CGFloat) -> some View`

Sets the minimum amount that text in this view scales down to fit in the
available space.

`var minimumScaleFactor: CGFloat`

The minimum permissible proportion to shrink the font size to fit the text
into the available space.

`func baselineOffset(CGFloat) -> some View`

Sets the vertical offset for the text relative to its baseline in this view.

`func kerning(CGFloat) -> some View`

Sets the spacing, or kerning, between characters for the text in this view.

`func tracking(CGFloat) -> some View`

Sets the tracking for the text in this view.

`func flipsForRightToLeftLayoutDirection(Bool) -> some View`

Sets whether this view mirrors its contents horizontally when the layout
direction is right-to-left.

`enum TextAlignment`

An alignment position for text along the horizontal axis.

Instance Method

# typesettingLanguage(_:isEnabled:)

Specifies the language for typesetting.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func typesettingLanguage(
        _ language: Locale.Language,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`language`

    

The explicit language to use for typesetting.

`isEnabled`

    

A Boolean value that indicates whether text langauge is added

## Return Value

A view with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t
match the device UI language. In that case it’s useful to specify a language
so line height, line breaking and spacing will respect the script used for
that language. For example:

Note: this language does not affect text localization.

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Instance Method

# typesettingLanguage(_:isEnabled:)

Specifies the language for typesetting.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func typesettingLanguage(
        _ language: TypesettingLanguage,
        isEnabled: Bool = true
    ) -> some View
    

##  Parameters

`language`

    

The language to use for typesetting.

`isEnabled`

    

A Boolean value that indicates whether text language is added

## Return Value

A view with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t
match the device UI language. In that case it’s useful to specify a language
so line height, line breaking and spacing will respect the script used for
that language. For example:

Note: this language does not affect text localized localization.

## See Also

### Localizing text

Preparing views for localization

Specify hints and add strings to localize your SwiftUI views.

`struct LocalizedStringKey`

The key used to look up an entry in a strings file or strings dictionary file.

`var locale: Locale`

The current locale that views should use.

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> some View`

Specifies the language for typesetting.

`struct TypesettingLanguage`

Defines how typesetting language is determined for text.

Instance Method

# lineLimit(_:)

Sets the maximum number of lines that text can occupy in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func lineLimit(_ number: Int?) -> some View
    

##  Parameters

`number`

    

The line limit. If `nil`, no line limit applies.

## Return Value

A view that limits the number of lines that `Text` instances display.

## Discussion

Use this modifier to cap the number of lines that an individual text element
can display.

The line limit applies to all `Text` instances within a hierarchy. For
example, an `HStack` with multiple pieces of text longer than three lines caps
each piece of text to three lines rather than capping the total number of
lines across the `HStack`.

In the example below, the modifier limits the very long line in the `Text`
element to the 2 lines that fit within the view’s bounds:

## See Also

### Limiting line count for multiline text

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:)

Sets to a partial range the number of lines that text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(_ limit: PartialRangeFrom<Int>) -> some View
    

##  Parameters

`limit`

    

The line limit.

## Discussion

Use this modifier to specify a partial range of lines that a `Text` view or a
vertical `TextField` can occupy. When the text of such views occupies less
space than the provided limit, that view expands to occupy the minimum number
of lines.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:)

Sets to a partial range the number of lines that text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(_ limit: PartialRangeThrough<Int>) -> some View
    

##  Parameters

`limit`

    

The line limit.

## Discussion

Use this modifier to specify a partial range of lines that a `Text` view or a
vertical `TextField` can occupy. When the text of such views occupies more
space than the provided limit, a `Text` view truncates its content while a
`TextField` becomes scrollable.

Note

This modifier is equivalent to the `lineLimit(_:)` modifier taking just an
integer.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:)

Sets to a closed range the number of lines that text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(_ limit: ClosedRange<Int>) -> some View
    

##  Parameters

`limit`

    

The line limit.

## Discussion

Use this modifier to specify a closed range of lines that a `Text` view or a
vertical `TextField` can occupy. When the text of such views occupies more
space than the provided limit, a `Text` view truncates its content while a
`TextField` becomes scrollable.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(Int, reservesSpace: Bool) -> some View`

Sets a limit for the number of lines text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineLimit(_:reservesSpace:)

Sets a limit for the number of lines text can occupy in this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func lineLimit(
        _ limit: Int,
        reservesSpace: Bool
    ) -> some View
    

##  Parameters

`limit`

    

The line limit.

`reservesSpace`

    

Whether text reserves space so that it always occupies the height required to
display the specified number of lines.

## Discussion

Use this modifier to specify a limit to the lines that a `Text` or a vertical
`TextField` may occupy. If passed a value of true for the `reservesSpace`
parameter, and the text of such views occupies less space than the provided
limit, that view expands to occupy the minimum number of lines. When the text
occupies more space than the provided limit, a `Text` view truncates its
content while a `TextField` becomes scrollable.

## See Also

### Limiting line count for multiline text

`func lineLimit(Int?) -> some View`

Sets the maximum number of lines that text can occupy in this view.

`func lineLimit(PartialRangeFrom<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(PartialRangeThrough<Int>) -> some View`

Sets to a partial range the number of lines that text can occupy in this view.

`func lineLimit(ClosedRange<Int>) -> some View`

Sets to a closed range the number of lines that text can occupy in this view.

`var lineLimit: Int?`

The maximum number of lines that text can occupy in a view.

Instance Method

# lineSpacing(_:)

Sets the amount of space between lines of text in this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func lineSpacing(_ lineSpacing: CGFloat) -> some View
    

##  Parameters

`lineSpacing`

    

The amount of space between the bottom of one line and the top of the next
line in points.

## Discussion

Use `lineSpacing(_:)` to set the amount of spacing from the bottom of one line
to the top of the next for text elements in the view.

In the `Text` view in the example below, 10 points separate the bottom of one
line to the top of the next as the text field wraps inside this view. Applying
`lineSpacing(_:)` to a view hierarchy applies the line spacing to all text
elements contained in the view.

## See Also

### Formatting multiline text

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`func multilineTextAlignment(TextAlignment) -> some View`

Sets the alignment of a text view that contains multiple lines of text.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

Instance Method

# multilineTextAlignment(_:)

Sets the alignment of a text view that contains multiple lines of text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func multilineTextAlignment(_ alignment: TextAlignment) -> some View
    

##  Parameters

`alignment`

    

A value that you use to align multiple lines of text within a view.

## Return Value

A view that aligns the lines of multiline `Text` instances it contains.

## Discussion

Use this modifier to set an alignment for a multiline block of text. For
example, the modifier centers the contents of the following `Text` view:

The text in the above example spans more than one line because:

  * The newline character introduces a line break.

  * The frame modifier limits the space available to the text view, and by default a text view wraps lines that don’t fit in the available width. As a result, the text before the explicit line break wraps to three lines, and the text after uses two lines.

The modifier applies the alignment to the all the lines of text in the view,
regardless of why wrapping occurs:

The modifier has no effect on a `Text` view that contains only one line of
text, because a text view has a width that exactly matches the width of its
widest line. If you want to align an entire text view rather than its
contents, set the aligment of its container, like a `VStack` or a frame that
you create with the
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
modifier.

Note

You can use this modifier to control the alignment of a `Text` view that you
create with the `init(_:style:)` initializer to display localized dates and
times, including when the view uses only a single line, but only when that
view appears in a widget.

The modifier also affects the content alignment of other text container types,
like `TextEditor` and `TextField`. In those cases, the modifier sets the
alignment even when the view contains only a single line because view’s width
isn’t dictated by the width of the text it contains.

The modifier operates by setting the `multilineTextAlignment` value in the
environment, so it affects all the text containers in the modified view
hierarchy. For example, you can apply the modifier to a `VStack` to configure
all the text views inside the stack.

## See Also

### Formatting multiline text

`func lineSpacing(CGFloat) -> some View`

Sets the amount of space between lines of text in this view.

`var lineSpacing: CGFloat`

The distance in points between the bottom of one line fragment and the top of
the next.

`var multilineTextAlignment: TextAlignment`

An environment value that indicates how a text view aligns its lines when the
content wraps or contains newlines.

Instance Method

# textSelection(_:)

Controls whether people can select text within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func textSelection<S>(_ selectability: S) -> some View where S : TextSelectability
    

## Discussion

People sometimes need to copy useful information from `Text` views — including
error messages, serial numbers, or IP addresses — so they can then paste the
text into another context. Enable text selection to let people select text in
a platform-appropriate way.

You can apply this method to an individual text view, or to a container to
make each contained text view selectable. In the following example, the person
using the app can select text that shows the date of an event or the name or
email of any of the event participants:

On macOS, people use the mouse or trackpad to select a range of text, which
they can quickly copy by choosing Edit > Copy, or with the standard keyboard
shortcut.

On iOS, the person using the app touches and holds on a selectable `Text`
view, which brings up a system menu with menu items appropriate for the
current context. These menu items operate on the entire contents of the `Text`
view; the person can’t select a range of text like they can on macOS.

Note

`Button` views don’t support text selection.

## See Also

### Selecting text

`protocol TextSelectability`

A type that describes the ability to select text.

Instance Method

# autocorrectionDisabled(_:)

Sets whether to disable autocorrection for this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func autocorrectionDisabled(_ disable: Bool = true) -> some View
    

##  Parameters

`disable`

    

A Boolean value that indicates whether autocorrection is disabled for this
view. The default value is `true`.

## Discussion

Use this method when the effect of autocorrection would make it more difficult
for the user to input information. The entry of proper names and street
addresses are examples where autocorrection can negatively affect the user’s
ability complete a data entry task.

The example below configures a `TextField` with the default keyboard.
Disabling autocorrection allows the user to enter arbitrary text without the
autocorrection system offering suggestions or attempting to override their
input.

## See Also

### Managing text entry

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# keyboardType(_:)

Sets the keyboard type for this view.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    func keyboardType(_ type: UIKeyboardType) -> some View
    

##  Parameters

`type`

    

One of the keyboard types defined in the `UIKeyboardType` enumeration.

## Discussion

Use `keyboardType(_:)` to specify the keyboard type to use for text entry. A
number of different keyboard types are available to meet specialized input
needs, such as entering email addresses or phone numbers.

The example below presents a `TextField` to input an email address. Setting
the text field’s keyboard type to `.emailAddress` ensures the user can only
enter correctly formatted email addresses.

There are several different kinds of specialized keyboard types available
though the `UIKeyboardType` enumeration. To specify the default system
keyboard type, use `.default`.

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# scrollDismissesKeyboard(_:)

Configures the behavior in which scrollable content interacts with the
software keyboard.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+

    
    
    func scrollDismissesKeyboard(_ mode: ScrollDismissesKeyboardMode) -> some View
    

##  Parameters

`mode`

    

The keyboard dismissal mode that scrollable content uses.

## Return Value

A view that uses the specified keyboard dismissal mode.

## Discussion

You use this modifier to customize how scrollable content interacts with the
software keyboard. For example, you can specify a value of `immediately` to
indicate that you would like scrollable content to immediately dismiss the
keyboard if present when a scroll drag gesture begins.

You can also use this modifier to customize the keyboard dismissal behavior
for other kinds of scrollable views, like a `List` or a `TextEditor`.

By default, a `TextEditor` is interactive while other kinds of scrollable
content always dismiss the keyboard on a scroll when linked against iOS 16 or
later. Pass a value of `never` to indicate that scrollable content should
never automatically dismiss the keyboard.

## See Also

### Interacting with a software keyboard

`var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode`

The way that scrollable content interacts with the software keyboard.

`struct ScrollDismissesKeyboardMode`

The ways that scrollable content can interact with the software keyboard.

Instance Method

# textInputAutocapitalization(_:)

Sets how often the shift key in the keyboard is automatically enabled.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func textInputAutocapitalization(_ autocapitalization: TextInputAutocapitalization?) -> some View
    

##  Parameters

`autocapitalization`

    

One of the capitalizing behaviors defined in the `TextInputAutocapitalization`
struct or nil.

## Discussion

Use `textInputAutocapitalization(_:)` when you need to automatically
capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text the shift key is automatically
enabled before every word:

The `TextInputAutocapitalization` struct defines the available
autocapitalizing behavior. Providing `nil` to this view modifier does not
change the autocapitalization behavior. The default is
`TextInputAutocapitalization.sentences`.

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# textContentType(_:)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    func textContentType(_ textContentType: UITextContentType?) -> some View
    

##  Parameters

`textContentType`

    

One of the content types available in the `UITextContentType` structure that
identify the semantic meaning expected for a text-entry area. These include
support for email addresses, location names, URLs, and telephone numbers, to
name just a few.

## Discussion

Use this method to set the content type for input text. For example, you can
configure a `TextField` for the entry of email addresses:

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# textContentType(_:)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

macOS 11.0+

    
    
    func textContentType(_ textContentType: NSTextContentType?) -> some View
    

##  Parameters

`textContentType`

    

One of the content types available in the `NSTextContentType` structure that
identify the semantic meaning expected for a text-entry area.

## Discussion

Use this method to set the content type for input text. For example, you can
configure a `TextField` for the entry of a username:

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(WKTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# textContentType(_:)

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on a watchOS device.

watchOS 6.0+

    
    
    func textContentType(_ textContentType: WKTextContentType?) -> some View
    

##  Parameters

`textContentType`

    

One of the content types available in the `WKTextContentType` structure that
identify the semantic meaning expected for a text-entry area. These include
support for email addresses, location names, URLs, and telephone numbers, to
name just a few.

## Discussion

Use this method to set the content type for input text. For example, you can
configure a `TextField` for the entry of email addresses:

## See Also

### Managing text entry

`func autocorrectionDisabled(Bool) -> some View`

Sets whether to disable autocorrection for this view.

`var autocorrectionDisabled: Bool`

A Boolean value that determines whether the view hierarchy has auto-correction
enabled.

`func keyboardType(UIKeyboardType) -> some View`

Sets the keyboard type for this view.

`func scrollDismissesKeyboard(ScrollDismissesKeyboardMode) -> some View`

Configures the behavior in which scrollable content interacts with the
software keyboard.

`func textContentType(UITextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on an iOS or tvOS device.

`func textContentType(NSTextContentType?) -> some View`

Sets the text content type for this view, which the system uses to offer
suggestions while the user enters text on macOS.

`func textInputAutocapitalization(TextInputAutocapitalization?) -> some View`

Sets how often the shift key in the keyboard is automatically enabled.

`struct TextInputAutocapitalization`

The kind of autocapitalization behavior applied during text input.

Instance Method

# findNavigator(isPresented:)

Programmatically presents the find and replace interface for text editor
views.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func findNavigator(isPresented: Binding<Bool>) -> some View
    

##  Parameters

`isPresented`

    

A binding to a Boolean value that controls the presentation of the find and
replace interface.

## Return Value

A view that presents the find and replace interface when `isPresented` is
`true`.

## Discussion

Add this modifier to a `TextEditor`, or to a view hierarchy that contains at
least one text editor, to control the presentation of the find and replace
interface. When you set the `isPresented` binding to `true`, the system shows
the interface, and when you set it to `false`, the system hides the interface.
The following example shows and hides the interface based on the state of a
toolbar button:

The find and replace interface allows people to search for instances of a
specified string in the text editor, and optionally to replace instances of
the search string with another string. They can also show and hide the
interface using built-in controls, like menus and keyboard shortcuts. SwiftUI
updates `isPresented` to reflect the users’s actions.

If the text editor view isn’t currently in focus, the system still presents
the find and replace interface when you set `isPresented` to `true`. If the
view hierarchy contains multiple editors, the one that shows the find and
replace interface is nondeterministic.

You can disable the find and replace interface for a text editor by applying
the `findDisabled(_:)` modifier to the editor. If you do that, setting this
modifier’s `isPresented` binding to `true` has no effect, but only if the
disabling modifier appears closer to the text editor, like this:

## See Also

### Searching for text in a view with find and replace

`func findDisabled(Bool) -> some View`

Prevents find and replace operations in a text editor.

`func replaceDisabled(Bool) -> some View`

Prevents replace operations in a text editor.

Instance Method

# findDisabled(_:)

Prevents find and replace operations in a text editor.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func findDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether to disable the find and replace
interface for a text editor.

## Return Value

A view that disables the find and replace interface.

## Discussion

Add this modifier to ensure that people can’t activate the find and replace
interface for a `TextEditor`:

When you disable the find operation, you also implicitly disable the replace
operation. If you want to only disable replace, use `replaceDisabled(_:)`
instead.

Using this modifer also prevents programmatic find and replace interface
presentation using the `findNavigator(isPresented:)` method. Be sure to place
the disabling modifier closer to the text editor for this to work:

If you apply this modifer at multiple levels of a view hierarchy, the call
closest to the text editor takes precedence. For example, people can activate
find and replace for the first text editor in the following example, but not
the second:

## See Also

### Searching for text in a view with find and replace

`func findNavigator(isPresented: Binding<Bool>) -> some View`

Programmatically presents the find and replace interface for text editor
views.

`func replaceDisabled(Bool) -> some View`

Prevents replace operations in a text editor.

Instance Method

# replaceDisabled(_:)

Prevents replace operations in a text editor.

iOS 16.0+  iPadOS 16.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func replaceDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that indicates whether text replacement in the find and
replace interface is disabled.

## Return Value

A view that disables the replace feature of a find and replace interface.

## Discussion

Add this modifier to ensure that people can’t activate the replace feature of
a find and replace interface for a `TextEditor`:

If you want to disable both find and replace, use the `findDisabled(_:)`
modifier instead.

Using this modifer also disables the replace feature of a find and replace
interface that you present programmatically using the
`findNavigator(isPresented:)` method. Be sure to place the disabling modifier
closer to the text editor for this to work:

If you apply this modifer at multiple levels of a view hierarchy, the call
closest to the text editor takes precedence. For example, people can activate
find and replace for the first text editor in the following example, but only
find for the second:

## See Also

### Searching for text in a view with find and replace

`func findNavigator(isPresented: Binding<Bool>) -> some View`

Programmatically presents the find and replace interface for text editor
views.

`func findDisabled(Bool) -> some View`

Prevents find and replace operations in a text editor.

Instance Method

# symbolRenderingMode(_:)

Sets the rendering mode for symbol images within this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> some View
    

##  Parameters

`mode`

    

The symbol rendering mode to use.

## Return Value

A view that uses the rendering mode you supply.

## See Also

### Setting symbol rendering modes

`var symbolRenderingMode: SymbolRenderingMode?`

The current symbol rendering mode, or `nil` denoting that the mode is picked
automatically using the current image and foreground style as parameters.

`struct SymbolRenderingMode`

A symbol rendering mode.

Instance Method

# symbolVariant(_:)

Makes symbols within the view show a particular variant.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func symbolVariant(_ variant: SymbolVariants) -> some View
    

##  Parameters

`variant`

    

The variant to use for symbols. Use the values in `SymbolVariants`.

## Return Value

A view that applies the specified symbol variant or variants to itself and its
child views.

## Discussion

When you want all the SF Symbols in a part of your app’s user interface to use
the same variant, use the `symbolVariant(_:)` modifier with a `SymbolVariants`
value, like `fill`:

A symbol that doesn’t have the specified variant remains unaffected. In the
example above, the `list.bullet` symbol doesn’t have a filled variant, so the
`symbolVariant(_:)` modifer has no effect.

If you apply the modifier more than once, its effects accumulate.
Alternatively, you can apply multiple variants in one call:

All of the labels in the code above produce the same output:

You can apply all these variants in any order, but if you apply more than one
shape variant, the one closest to the symbol takes precedence. For example,
the following image uses the `square` shape:

To cause a symbol to ignore the variants currently in the environment,
directly set the `symbolVariants` environment value to `none` using the
`environment(_:_:)` modifer.

## See Also

### Setting a symbol variant

`var symbolVariants: SymbolVariants`

The symbol variant to use in this environment.

`struct SymbolVariants`

A variant of a symbol.


Initializer

# init(_:tableName:bundle:comment:)

Creates a text view that displays localized content identified by a key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        _ key: LocalizedStringKey,
        tableName: String? = nil,
        bundle: Bundle? = nil,
        comment: StaticString? = nil
    )

##  Parameters

`key`

    

The key for a string in the table identified by `tableName`.

`tableName`

    

The name of the string table to search. If `nil`, use the table in the
`Localizable.strings` file.

`bundle`

    

The bundle containing the strings file. If `nil`, use the main bundle.

`comment`

    

Contextual information about this key-value pair.

## Discussion

Use this initializer to look for the `key` parameter in a localization table
and display the associated string value in the initialized text view. If the
initializer can’t find the key in the table, or if no table exists, the text
view displays the string representation of the key instead.

When you initialize a text view with a string literal, the view triggers this
initializer because it assumes you want the string localized, even when you
don’t explicitly specify a table, as in the above example. If you haven’t
provided localization for a particular string, you still get reasonable
behavior, because the initializer displays the key, which typically contains
the unlocalized string.

If you initialize a text view with a string variable rather than a string
literal, the view triggers the `init(_:)` initializer instead, because it
assumes that you don’t want localization in that case. If you do want to
localize the value stored in a string variable, you can choose to call the
`init(_:tableName:bundle:comment:)` initializer by first creating a
`LocalizedStringKey` instance from the string variable:

If you have a string literal that you don’t want to localize, use the
`init(verbatim:)` initializer instead.

### Styling localized strings with markdown

If the localized string or the fallback key contains Markdown, the view
displays the text with appropriate styling. For example, consider an app with
the following entry in its Spanish localization file:

You can create a `Text` view with the Markdown-formatted base language version
of the string as the localization key, like this:

When viewed in a Spanish locale, the view uses the Spanish text from the
strings file, applying the Markdown styling.

Important

`Text` doesn’t render all styling possible in Markdown. It doesn’t support
line breaks, soft breaks, or any style of paragraph- or block-based formatting
like lists, block quotes, code blocks, or tables. It also doesn’t support the
`imageURL` attribute. Parsing with SwiftUI treats any whitespace in the
Markdown string as described by the
`AttributedString.MarkdownParsingOptions.InterpretedSyntax.inlineOnlyPreservingWhitespace`
parsing option.

## See Also

### Creating a text view from a string

`init(LocalizedStringResource)`

Creates a text view that displays a localized string resource.

`init<S>(S)`

Creates a text view that displays a stored string without localization.

`init(verbatim: String)`

Creates a text view that displays a string literal without localization.

Initializer

# init(_:)

Creates a text view that displays a localized string resource.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ resource: LocalizedStringResource)

## Discussion

Use this initializer to display a localized string that is represented by a
`LocalizedStringResource`

## See Also

### Creating a text view from a string

`init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment:
StaticString?)`

Creates a text view that displays localized content identified by a key.

`init<S>(S)`

Creates a text view that displays a stored string without localization.

`init(verbatim: String)`

Creates a text view that displays a string literal without localization.

Initializer

# init(_:)

Creates a text view that displays a stored string without localization.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init<S>(_ content: S) where S : StringProtocol

##  Parameters

`content`

    

The string value to display without localization.

## Discussion

Use this initializer to create a text view that displays — without
localization — the text in a string variable.

SwiftUI doesn’t call the `init(_:)` method when you initialize a text view
with a string literal as the input. Instead, a string literal triggers the
`init(_:tableName:bundle:comment:)` method — which treats the input as a
`LocalizedStringKey` instance — and attempts to perform localization.

By default, SwiftUI assumes that you don’t want to localize stored strings,
but if you do, you can first create a localized string key from the value, and
initialize the text view with that. Using a key as input triggers the
`init(_:tableName:bundle:comment:)` method instead.

## See Also

### Creating a text view from a string

`init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment:
StaticString?)`

Creates a text view that displays localized content identified by a key.

`init(LocalizedStringResource)`

Creates a text view that displays a localized string resource.

`init(verbatim: String)`

Creates a text view that displays a string literal without localization.

Initializer

# init(verbatim:)

Creates a text view that displays a string literal without localization.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(verbatim content: String)

##  Parameters

`content`

    

A string to display without localization.

## Discussion

Use this initializer to create a text view with a string literal without
performing localization:

If you want to localize a string literal before displaying it, use the
`init(_:tableName:bundle:comment:)` initializer instead. If you want to
display a string variable, use the `init(_:)` initializer, which also bypasses
localization.

## See Also

### Creating a text view from a string

`init(LocalizedStringKey, tableName: String?, bundle: Bundle?, comment:
StaticString?)`

Creates a text view that displays localized content identified by a key.

`init(LocalizedStringResource)`

Creates a text view that displays a localized string resource.

`init<S>(S)`

Creates a text view that displays a stored string without localization.

Initializer

# init(_:)

Creates a text view that displays styled attributed content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(_ attributedContent: AttributedString)

##  Parameters

`attributedContent`

    

An attributed string to style and display, in accordance with its attributes.

## Discussion

Use this initializer to style text according to attributes found in the
specified `AttributedString`. Attributes in the attributed string take
precedence over styles added by view modifiers. For example, the attributed
text in the following example appears in blue, despite the use of the
`foregroundColor(_:)` modifier to use red throughout the enclosing `VStack`:

SwiftUI combines text attributes with SwiftUI modifiers whenever possible. For
example, the following listing creates text that is both bold and red:

A SwiftUI `Text` view renders most of the styles defined by the Foundation
attribute `inlinePresentationIntent`, like the `stronglyEmphasized` value,
which SwiftUI presents as bold text.

Important

`Text` uses only a subset of the attributes defined in
`AttributeScopes.FoundationAttributes`. `Text` renders all
`InlinePresentationIntent` attributes except for `lineBreak` and `softBreak`.
It also renders the `link` attribute as a clickable link. `Text` ignores any
other Foundation-defined attributes in an attributed string.

SwiftUI also defines additional attributes in the attribute scope
`AttributeScopes.SwiftUIAttributes` which you can access from an attributed
string’s `swiftUI` property. SwiftUI attributes take precedence over
equivalent attributes from other frameworks, such as
`AttributeScopes.UIKitAttributes` and `AttributeScopes.AppKitAttributes`.

You can create an `AttributedString` with Markdown syntax, which allows you to
style distinct runs within a `Text` view:

The `**` syntax around “Thank You!” applies an `inlinePresentationIntent`
attribute with the value `stronglyEmphasized`. SwiftUI renders this as bold
text, as described earlier. The link syntax around “website” creates a `link`
attribute, which `Text` styles to indicate it’s a link; by default, clicking
or tapping the link opens the linked URL in the user’s default browser.
Alternatively, you can perform custom link handling by putting an
`OpenURLAction` in the text view’s environment.

You can also use Markdown syntax in localized string keys, which means you can
write the above example without needing to explicitly create an
`AttributedString`:

In your app’s strings files, use Markdown syntax to apply styling to the app’s
localized strings. You also use this approach when you want to perform
automatic grammar agreement on localized strings, with the
`^[text](inflect:true)` syntax.

For details about Markdown syntax support in SwiftUI, see
`init(_:tableName:bundle:comment:)`.

Initializer

# init(_:)

Creates an instance that displays a localized range between two dates.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ dates: ClosedRange<Date>)

##  Parameters

`dates`

    

The range of dates to display

## See Also

### Creating a text view for a date

`init(DateInterval)`

Creates an instance that displays a localized time interval.

`init(Date, style: Text.DateStyle)`

Creates an instance that displays localized dates and times using a specific
style.

Initializer

# init(_:)

Creates an instance that displays a localized time interval.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ interval: DateInterval)

##  Parameters

`interval`

    

The date interval to display

## Discussion

Example output: 9:30AM - 3:30PM

## See Also

### Creating a text view for a date

`init(ClosedRange<Date>)`

Creates an instance that displays a localized range between two dates.

`init(Date, style: Text.DateStyle)`

Creates an instance that displays localized dates and times using a specific
style.

Initializer

# init(_:style:)

Creates an instance that displays localized dates and times using a specific
style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ date: Date,
        style: Text.DateStyle
    )

##  Parameters

`date`

    

The target date to display.

`style`

    

The style used when displaying a date.

## See Also

### Creating a text view for a date

`init(ClosedRange<Date>)`

Creates an instance that displays a localized range between two dates.

`init(DateInterval)`

Creates an instance that displays a localized time interval.

Initializer

# init(_:format:)

Creates a text view that displays the formatted representation of a nonstring
type supported by a corresponding format style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<F>(
        _ input: F.FormatInput,
        format: F
    ) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String

##  Parameters

`input`

    

The underlying value to display.

`format`

    

A format style of type `F` to convert the underlying value of type
`F.FormatInput` to a string representation.

## Discussion

Use this initializer to create a text view backed by a nonstring value, using
a `FormatStyle` to convert the type to a string representation. Any changes to
the value update the string displayed by the text view.

In the following example, three `Text` views present a date with different
combinations of date and time fields, by using different `Date.FormatStyle`
options.

## See Also

### Creating a text view with formatting

`init<Subject>(Subject, formatter: Formatter)`

Creates a text view that displays the formatted representation of a reference-
convertible value.

`init<Subject>(Subject, formatter: Formatter)`

Creates a text view that displays the formatted representation of a Foundation
object.

Initializer

# init(_:formatter:)

Creates a text view that displays the formatted representation of a reference-
convertible value.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<Subject>(
        _ subject: Subject,
        formatter: Formatter
    ) where Subject : ReferenceConvertible

##  Parameters

`subject`

    

A `ReferenceConvertible` instance compatible with `formatter`.

`formatter`

    

A `Formatter` capable of converting `subject` into a string representation.

## Discussion

Use this initializer to create a text view that formats `subject` using
`formatter`.

## See Also

### Creating a text view with formatting

`init<F>(F.FormatInput, format: F)`

Creates a text view that displays the formatted representation of a nonstring
type supported by a corresponding format style.

`init<Subject>(Subject, formatter: Formatter)`

Creates a text view that displays the formatted representation of a Foundation
object.

Initializer

# init(_:formatter:)

Creates a text view that displays the formatted representation of a Foundation
object.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<Subject>(
        _ subject: Subject,
        formatter: Formatter
    ) where Subject : NSObject

##  Parameters

`subject`

    

An `NSObject` instance compatible with `formatter`.

`formatter`

    

A `Formatter` capable of converting `subject` into a string representation.

## Discussion

Use this initializer to create a text view that formats `subject` using
`formatter`.

## See Also

### Creating a text view with formatting

`init<F>(F.FormatInput, format: F)`

Creates a text view that displays the formatted representation of a nonstring
type supported by a corresponding format style.

`init<Subject>(Subject, formatter: Formatter)`

Creates a text view that displays the formatted representation of a reference-
convertible value.

Initializer

# init(_:)

Creates an instance that wraps an `Image`, suitable for concatenating with
other `Text`

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ image: Image)

Initializer

# init(timerInterval:pauseTime:countsDown:showsHours:)

Creates an instance that displays a timer counting within the provided
interval.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        timerInterval: ClosedRange<Date>,
        pauseTime: Date? = nil,
        countsDown: Bool = true,
        showsHours: Bool = true
    )

##  Parameters

`timerInterval`

    

The interval between where to run the timer.

`pauseTime`

    

If present, the date at which to pause the timer. The default is `nil` which
indicates to never pause.

`countsDown`

    

Whether to count up or down. The default is `true`.

`showsHours`

    

Whether to include an hours component if there are more than 60 minutes left
on the timer. The default is `true`.

## Discussion

The example above shows a text that displays a timer counting down from
“12:00” and will pause when reaching “10:00”.

Instance Method

# font(_:)

Sets the default font for text in the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func font(_ font: Font?) -> Text

##  Parameters

`font`

    

The font to use when displaying this text.

## Return Value

Text that uses the font you specify.

## Discussion

Use `font(_:)` to apply a specific font to an individual Text View, or all of
the text views in a container.

In the example below, the first text field has a font set directly, while the
font applied to the following container applies to all of the text views
inside that container:

## See Also

### Choosing a font

`func fontWeight(Font.Weight?) -> Text`

Sets the font weight of the text.

`func fontDesign(Font.Design?) -> Text`

Sets the font design of the text.

`func fontWidth(Font.Width?) -> Text`

Sets the font width of the text.

Instance Method

# fontWeight(_:)

Sets the font weight of the text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fontWeight(_ weight: Font.Weight?) -> Text

##  Parameters

`weight`

    

One of the available font weights.

## Return Value

Text that uses the font weight you specify.

## See Also

### Choosing a font

`func font(Font?) -> Text`

Sets the default font for text in the view.

`func fontDesign(Font.Design?) -> Text`

Sets the font design of the text.

`func fontWidth(Font.Width?) -> Text`

Sets the font width of the text.

Instance Method

# fontDesign(_:)

Sets the font design of the text.

iOS 16.1+  iPadOS 16.1+  macOS 13.0+  Mac Catalyst 16.1+  tvOS 16.1+  watchOS
9.1+  visionOS 1.0+

    
    
    func fontDesign(_ design: Font.Design?) -> Text

##  Parameters

`design`

    

One of the available font designs.

## Return Value

Text that uses the font design you specify.

## See Also

### Choosing a font

`func font(Font?) -> Text`

Sets the default font for text in the view.

`func fontWeight(Font.Weight?) -> Text`

Sets the font weight of the text.

`func fontWidth(Font.Width?) -> Text`

Sets the font width of the text.

Instance Method

# fontWidth(_:)

Sets the font width of the text.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func fontWidth(_ width: Font.Width?) -> Text

##  Parameters

`width`

    

One of the available font widths.

## Return Value

Text that uses the font width you specify, if available.

## See Also

### Choosing a font

`func font(Font?) -> Text`

Sets the default font for text in the view.

`func fontWeight(Font.Weight?) -> Text`

Sets the font weight of the text.

`func fontDesign(Font.Design?) -> Text`

Sets the font design of the text.

Instance Method

# foregroundStyle(_:)

Sets the style of the text displayed by this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func foregroundStyle<S>(_ style: S) -> Text where S : ShapeStyle

##  Parameters

`style`

    

The style to use when displaying this text.

## Return Value

A text view that uses the color value you supply.

## Discussion

Use this method to change the rendering style of the text rendered by a text
view.

For example, you can display the names of the colors red, green, and blue in
their respective colors:

## See Also

### Styling the view’s text

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# bold()

Applies a bold font weight to the text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func bold() -> Text

## Return Value

Bold text.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# bold(_:)

Applies a bold font weight to the text.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func bold(_ isActive: Bool) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether text has bold styling.

## Return Value

Bold text.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# italic()

Applies italics to the text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func italic() -> Text

## Return Value

Italic text.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# italic(_:)

Applies italics to the text.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func italic(_ isActive: Bool) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether italic styling is added.

## Return Value

Italic text.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# strikethrough(_:color:)

Applies a strikethrough to the text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func strikethrough(
        _ isActive: Bool = true,
        color: Color? = nil
    ) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether the text has a strikethrough applied.

`color`

    

The color of the strikethrough. If `color` is `nil`, the strikethrough uses
the default foreground color.

## Return Value

Text with a line through its center.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# strikethrough(_:pattern:color:)

Applies a strikethrough to the text.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func strikethrough(
        _ isActive: Bool = true,
        pattern: Text.LineStyle.Pattern,
        color: Color? = nil
    ) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether strikethrough is added. The default
value is `true`.

`pattern`

    

The pattern of the line.

`color`

    

The color of the strikethrough. If `color` is `nil`, the strikethrough uses
the default foreground color.

## Return Value

Text with a line through its center.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# underline(_:color:)

Applies an underline to the text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func underline(
        _ isActive: Bool = true,
        color: Color? = nil
    ) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether the text has an underline.

`color`

    

The color of the underline. If `color` is `nil`, the underline uses the
default foreground color.

## Return Value

Text with a line running along its baseline.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# underline(_:pattern:color:)

Applies an underline to the text.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func underline(
        _ isActive: Bool = true,
        pattern: Text.LineStyle.Pattern,
        color: Color? = nil
    ) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether underline styling is added. The default
value is `true`.

`pattern`

    

The pattern of the line.

`color`

    

The color of the underline. If `color` is `nil`, the underline uses the
default foreground color.

## Return Value

Text with a line running along its baseline.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# monospaced(_:)

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

iOS 16.4+  iPadOS 16.4+  macOS 13.3+  Mac Catalyst 16.4+  tvOS 16.4+  watchOS
9.4+  visionOS 1.0+

    
    
    func monospaced(_ isActive: Bool = true) -> Text

##  Parameters

`isActive`

    

A Boolean value that indicates whether monospaced styling is added. Default
value is `true`.

## Return Value

Monospaced text.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# monospacedDigit()

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func monospacedDigit() -> Text

## Return Value

A text view with a modified font that uses fixed-width numeric characters,
while leaving other characters proportionally spaced.

## Discussion

This modifier only affects numeric characters, and leaves all other characters
unchanged.

The following example shows the effect of `monospacedDigit()` on a text view.
It arranges two text views in a `VStack`, each displaying a formatted date
that contains many instances of the character 1. The second text view uses the
`monospacedDigit()`. Because 1 is usually a narrow character in proportional
fonts, applying the modifier widens all of the 1s, and the text view as a
whole. The non-digit characters in the text view remain unaffected.

If the base font of the text view doesn’t support fixed-width digits, the font
remains unchanged.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# kerning(_:)

Sets the spacing, or kerning, between characters.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func kerning(_ kerning: CGFloat) -> Text

##  Parameters

`kerning`

    

The spacing to use between individual characters in this text. Value of `0`
sets the kerning to the system default value.

## Return Value

Text with the specified amount of kerning.

## Discussion

Kerning defines the offset, in points, that a text view should shift
characters from the default spacing. Use positive kerning to widen the spacing
between characters. Use negative kerning to tighten the spacing between
characters.

The last character in the first case, which uses negative kerning, experiences
cropping because the kerning affects the trailing edge of the text view as
well.

Kerning attempts to maintain ligatures. For example, the Hoefler Text font
uses a ligature for the letter combination _ffl_ , as in the word _raffle_ ,
shown here with a small negative and a small positive kerning:

The _ffl_ letter combination keeps a constant shape as the other letters move
together or apart. Beyond a certain point in either direction, however,
kerning does disable nonessential ligatures.

Important

If you add both the `tracking(_:)` and `kerning(_:)` modifiers to a view, the
view applies the tracking and ignores the kerning.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# tracking(_:)

Sets the tracking for the text.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func tracking(_ tracking: CGFloat) -> Text

##  Parameters

`tracking`

    

The amount of additional space, in points, that the view should add to each
character cluster after layout. Value of `0` sets the tracking to the system
default value.

## Return Value

Text with the specified amount of tracking.

## Discussion

Tracking adds space, measured in points, between the characters in the text
view. A positive value increases the spacing between characters, while a
negative value brings the characters closer together.

The code above uses an unusually large amount of tracking to make it easy to
see the effect.

The effect of tracking resembles that of the `kerning(_:)` modifier, but adds
or removes trailing whitespace, rather than changing character offsets. Also,
using any nonzero amount of tracking disables nonessential ligatures, whereas
kerning attempts to maintain ligatures.

Important

If you add both the `tracking(_:)` and `kerning(_:)` modifiers to a view, the
view applies the tracking and ignores the kerning.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Instance Method

# baselineOffset(_:)

Sets the vertical offset for the text relative to its baseline.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func baselineOffset(_ baselineOffset: CGFloat) -> Text

##  Parameters

`baselineOffset`

    

The amount to shift the text vertically (up or down) relative to its baseline.

## Return Value

Text that’s above or below its baseline.

## Discussion

Change the baseline offset to move the text in the view (in points) up or down
relative to its baseline. The bounds of the view expand to contain the moved
text.

By drawing a border around each text view, you can see how the text moves, and
how that affects the view.

The first view, with a negative offset, grows downward to handle the lowered
text. The last view, with a positive offset, grows upward. The enclosing
`HStack` instance, shown in gray, ensures all the text views remain aligned at
their top edge, regardless of the offset.

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Enumeration

# Text.Case

A scheme for transforming the capitalization of characters within text.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    enum Case

## Topics

### Getting text cases

`case lowercase`

Displays text in all lowercase characters.

`case uppercase`

Displays text in all uppercase characters.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`struct DateStyle`

A predefined style used to display a `Date`.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Structure

# Text.DateStyle

A predefined style used to display a `Date`.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct DateStyle

## Topics

### Getting text date styles

`static let date: Text.DateStyle`

A style displaying a date.

`static let offset: Text.DateStyle`

A style displaying a date as offset from now.

`static let relative: Text.DateStyle`

A style displaying a date as relative to now.

`static let time: Text.DateStyle`

A style displaying only the time component for a date.

`static let timer: Text.DateStyle`

A style displaying a date as timer counting from now.

## Relationships

### Conforms To

  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Sendable`

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct LineStyle`

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

Structure

# Text.LineStyle

Description of the style used to draw the line for
`StrikethroughStyleAttribute` and `UnderlineStyleAttribute`.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct LineStyle

## Overview

Use this type to specify `underlineStyle` and `strikethroughStyle` SwiftUI
attributes of an `AttributedString`.

## Topics

### Getting text line styles

`static let single: Text.LineStyle`

Draw a single solid line.

### Creating a text line style

`init?(nsUnderlineStyle: NSUnderlineStyle)`

Creates a `Text.LineStyle` from `NSUnderlineStyle`.

`init(pattern: Text.LineStyle.Pattern, color: Color?)`

Creates a line style.

`struct Pattern`

The pattern, that the line has.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Styling the view’s text

`func foregroundStyle<S>(S) -> Text`

Sets the style of the text displayed by this view.

`func bold() -> Text`

Applies a bold font weight to the text.

`func bold(Bool) -> Text`

Applies a bold font weight to the text.

`func italic() -> Text`

Applies italics to the text.

`func italic(Bool) -> Text`

Applies italics to the text.

`func strikethrough(Bool, color: Color?) -> Text`

Applies a strikethrough to the text.

`func strikethrough(Bool, pattern: Text.LineStyle.Pattern, color: Color?) ->
Text`

Applies a strikethrough to the text.

`func underline(Bool, color: Color?) -> Text`

Applies an underline to the text.

`func underline(Bool, pattern: Text.LineStyle.Pattern, color: Color?) -> Text`

Applies an underline to the text.

`func monospaced(Bool) -> Text`

Modifies the font of the text to use the fixed-width variant of the current
font, if possible.

`func monospacedDigit() -> Text`

Modifies the text view’s font to use fixed-width digits, while leaving other
characters proportionally spaced.

`func kerning(CGFloat) -> Text`

Sets the spacing, or kerning, between characters.

`func tracking(CGFloat) -> Text`

Sets the tracking for the text.

`func baselineOffset(CGFloat) -> Text`

Sets the vertical offset for the text relative to its baseline.

`enum Case`

A scheme for transforming the capitalization of characters within text.

`struct DateStyle`

A predefined style used to display a `Date`.

Instance Method

# textScale(_:isEnabled:)

Applies a text scale to the text.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func textScale(
        _ scale: Text.Scale,
        isEnabled: Bool = true
    ) -> Text

##  Parameters

`scale`

    

The text scale to apply.

`isEnabled`

    

If true the text scale is applied; otherwise text scale is unchanged.

## Return Value

Text with the specified scale applied.

## See Also

### Fitting text into available space

`struct Scale`

Defines text scales

`enum TruncationMode`

The type of truncation to apply to a line of text when it’s too long to fit in
the available space.

Structure

# Text.Scale

Defines text scales

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct Scale

## Overview

Text scale provides a way to pick a logical text scale relative to the base
font which is used.

## Topics

### Gettingn built-in text scales

`static let `default`: Text.Scale`

Defines default text scale

`static let secondary: Text.Scale`

Defines secondary text scale

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Fitting text into available space

`func textScale(Text.Scale, isEnabled: Bool) -> Text`

Applies a text scale to the text.

`enum TruncationMode`

The type of truncation to apply to a line of text when it’s too long to fit in
the available space.

Enumeration

# Text.TruncationMode

The type of truncation to apply to a line of text when it’s too long to fit in
the available space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum TruncationMode

## Overview

When a text view contains more text than it’s able to display, the view might
truncate the text and place an ellipsis (…) at the truncation point. Use the
`truncationMode(_:)` modifier with one of the `TruncationMode` values to
indicate which part of the text to truncate, either at the beginning, in the
middle, or at the end.

## Topics

### Getting text truncation modes

`case head`

Truncate at the beginning of the line.

`case middle`

Truncate in the middle of the line.

`case tail`

Truncate at the end of the line.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Fitting text into available space

`func textScale(Text.Scale, isEnabled: Bool) -> Text`

Applies a text scale to the text.

`struct Scale`

Defines text scales

Instance Method

# typesettingLanguage(_:isEnabled:)

Specifies the language for typesetting.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func typesettingLanguage(
        _ language: TypesettingLanguage,
        isEnabled: Bool = true
    ) -> Text

##  Parameters

`language`

    

The language to use for typesetting.

`isEnabled`

    

A Boolean value that indicates whether text language is added

## Return Value

Text with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t
match the device UI language. In that case it’s useful to specify a language
so line height, line breaking and spacing will respect the script used for
that language. For example:

Note: this language does not affect text localized localization.

## See Also

### Localizing text

`func typesettingLanguage(Locale.Language, isEnabled: Bool) -> Text`

Specifies the language for typesetting.

Instance Method

# typesettingLanguage(_:isEnabled:)

Specifies the language for typesetting.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func typesettingLanguage(
        _ language: Locale.Language,
        isEnabled: Bool = true
    ) -> Text

##  Parameters

`language`

    

The explicit language to use for typesetting.

`isEnabled`

    

A Boolean value that indicates whether text langauge is added

## Return Value

Text with the typesetting language set to the value you supply.

## Discussion

In some cases `Text` may contain text of a particular language which doesn’t
match the device UI language. In that case it’s useful to specify a language
so line height, line breaking and spacing will respect the script used for
that language. For example:

Note: this language does not affect text localization.

## See Also

### Localizing text

`func typesettingLanguage(TypesettingLanguage, isEnabled: Bool) -> Text`

Specifies the language for typesetting.

Instance Method

# speechAdjustedPitch(_:)

Raises or lowers the pitch of spoken text.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAdjustedPitch(_ value: Double) -> Text

##  Parameters

`value`

    

The amount to raise or lower the pitch. Values between `-1` and `0` result in
a lower pitch while values between `0` and `1` result in a higher pitch. The
method clamps values to the range `-1` to `1`.

## Discussion

Use this modifier when you want to change the pitch of spoken text. The value
indicates how much higher or lower to change the pitch.

## See Also

### Configuring voiceover

`func speechAlwaysIncludesPunctuation(Bool) -> Text`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> Text`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> Text`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAlwaysIncludesPunctuation(_:)

Sets whether VoiceOver should always speak all punctuation in the text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAlwaysIncludesPunctuation(_ value: Bool = true) -> Text

##  Parameters

`value`

    

A Boolean value that you set to `true` if VoiceOver should speak all
punctuation in the text. Defaults to `true`.

## Discussion

Use this modifier to control whether the system speaks punctuation characters
in the text. You might use this for code or other text where the punctuation
is relevant, or where you want VoiceOver to speak a verbatim transcription of
the text you provide. For example, given the text:

VoiceOver would speak “All the world apostrophe s a stage comma and all the
men and women merely players semicolon”.

By default, VoiceOver voices punctuation based on surrounding context.

## See Also

### Configuring voiceover

`func speechAdjustedPitch(Double) -> Text`

Raises or lowers the pitch of spoken text.

`func speechAnnouncementsQueued(Bool) -> Text`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

`func speechSpellsOutCharacters(Bool) -> Text`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechAnnouncementsQueued(_:)

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechAnnouncementsQueued(_ value: Bool = true) -> Text

##  Parameters

`value`

    

A Boolean value that determines if VoiceOver speaks changes to text
immediately or enqueues them behind existing speech. Defaults to `true`.

## Discussion

Use this modifier when you want affect the order in which the accessibility
system delivers spoken text. Announcements can occur automatically when the
label or value of an accessibility element changes.

## See Also

### Configuring voiceover

`func speechAdjustedPitch(Double) -> Text`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> Text`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechSpellsOutCharacters(Bool) -> Text`

Sets whether VoiceOver should speak the contents of the text view character by
character.

Instance Method

# speechSpellsOutCharacters(_:)

Sets whether VoiceOver should speak the contents of the text view character by
character.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func speechSpellsOutCharacters(_ value: Bool = true) -> Text

##  Parameters

`value`

    

A Boolean value that when `true` indicates VoiceOver should speak text as
individual characters. Defaults to `true`.

## Discussion

Use this modifier when you want VoiceOver to speak text as individual letters,
character by character. This is important for text that is not meant to be
spoken together, like:

  * An acronym that isn’t a word, like APPL, spoken as “A-P-P-L”.

  * A number representing a series of digits, like 25, spoken as “two-five” rather than “twenty-five”.

## See Also

### Configuring voiceover

`func speechAdjustedPitch(Double) -> Text`

Raises or lowers the pitch of spoken text.

`func speechAlwaysIncludesPunctuation(Bool) -> Text`

Sets whether VoiceOver should always speak all punctuation in the text view.

`func speechAnnouncementsQueued(Bool) -> Text`

Controls whether to queue pending announcements behind existing speech rather
than interrupting speech in progress.

Operator

# +(_:_:)

Concatenates the text in two text views in a new text view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static func + (lhs: Text, rhs: Text) -> Text

##  Parameters

`lhs`

    

The first text view with text to combine.

`rhs`

    

The second text view with text to combine.

## Return Value

A new text view containing the combined contents of the two input text views.

Instance Method

# foregroundColor(_:)

Sets the color of the text displayed by this view.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    func foregroundColor(_ color: Color?) -> Text

Deprecated

Use `foregroundStyle(_:)` instead.

##  Parameters

`color`

    

The color to use when displaying this text.

## Return Value

A text view that uses the color value you supply.

## Discussion

Use this method to change the color of the text rendered by a text view.

For example, you can display the names of the colors red, green, and blue in
their respective colors:


Instance Method

# appendInterpolation(_:)

Appends a literal string segment to a string interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ string: String)

##  Parameters

`string`

    

The literal string to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends an attributed string to a string interpolation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ attributedString: AttributedString)

##  Parameters

`attributedString`

    

The attributed string to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

The following example shows how to use a string interpolation to format an
`AttributedString` and append it to static text. The resulting interpolation
implicitly creates a `LocalizedStringKey`, which a `Text` view uses to provide
its content.

For this example, assume that the app runs on a device set to a Russian
locale, and has the following entry in a Russian-localized
`Localizable.strings` file:

The attributed string `nextDate` replaces the format specifier `%@`,
maintaining its color and date-formatting attributes, when the `Text` view
renders its contents:

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation<T>(_ value: T) where T : _FormatSpecifiable

##  Parameters

`value`

    

A primitive type to append, such as `Int`, `UInt32`, or `Double`.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:specifier:)

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation<T>(
        _ value: T,
        specifier: String
    ) where T : _FormatSpecifiable

##  Parameters

`value`

    

The value to append.

`specifier`

    

A format specifier to convert `subject` to a string representation, like `%f`
for a `Double`, or `%x` to create a hexidecimal representation of a `UInt32`.
For a list of available specifier strings, see String Format Specifers.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends a date range to a string interpolation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ dates: ClosedRange<Date>)

##  Parameters

`dates`

    

The closed range of dates to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends a date interval to a string interpolation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ interval: DateInterval)

##  Parameters

`interval`

    

The date interval to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:format:)

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation<F>(
        _ input: F.FormatInput,
        format: F
    ) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String

##  Parameters

`input`

    

The instance to format and append.

`format`

    

A format style to use when converting `input` into a string representation.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

The following example shows how to use a string interpolation to format a
`Date` with a `Date.FormatStyle` and append it to static text. The resulting
interpolation implicitly creates a `LocalizedStringKey`, which a `Text` uses
to provide its content.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:formatter:)

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation<Subject>(
        _ subject: Subject,
        formatter: Formatter? = nil
    ) where Subject : NSObject

##  Parameters

`subject`

    

An `NSObject` to append.

`formatter`

    

A formatter to convert `subject` to a string representation.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

The following example shows how to use a `Measurement` value and a
`MeasurementFormatter` to create a `LocalizedStringKey` that uses the
formatter style `Formatter.UnitStyle.long` when generating the measurement’s
string representation. Rather than calling `appendInterpolation(_:formatter)`
directly, the code gets the formatting behavior implicitly by using the `\()`
string interpolation syntax.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:formatter:)

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation<Subject>(
        _ subject: Subject,
        formatter: Formatter? = nil
    ) where Subject : ReferenceConvertible

##  Parameters

`subject`

    

The Foundation object to append.

`formatter`

    

A formatter to convert `subject` to a string representation.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:style:)

Appends a formatted date to a string interpolation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(
        _ date: Date,
        style: Text.DateStyle
    )

##  Parameters

`date`

    

The date to append.

`style`

    

A predefined style to format the date with.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends the string displayed by a text view to a string interpolation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ text: Text)

##  Parameters

`value`

    

A `Text` instance to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends an image to a string interpolation.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ image: Image)

##  Parameters

`image`

    

The image to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(_:)

Appends the localized string resource to a string interpolation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(_ resource: LocalizedStringResource)

##  Parameters

`value`

    

The localized string resource to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)

Appends a timer interval to a string interpolation.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    mutating func appendInterpolation(
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

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendLiteral(String)`

Appends a literal string.

Instance Method

# appendLiteral(_:)

Appends a literal string.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    mutating func appendLiteral(_ literal: String)

##  Parameters

`literal`

    

The literal string to append.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting
string interpolations.

## See Also

### Appending to an interpolation

`func appendInterpolation(String)`

Appends a literal string segment to a string interpolation.

`func appendInterpolation(AttributedString)`

Appends an attributed string to a string interpolation.

`func appendInterpolation<T>(T)`

Appends a type, convertible to a string by using a default format specifier,
to a string interpolation.

`func appendInterpolation<T>(T, specifier: String)`

Appends a type, convertible to a string with a format specifier, to a string
interpolation.

`func appendInterpolation(ClosedRange<Date>)`

Appends a date range to a string interpolation.

`func appendInterpolation(DateInterval)`

Appends a date interval to a string interpolation.

`func appendInterpolation<F>(F.FormatInput, format: F)`

Appends the formatted representation of a nonstring type supported by a
corresponding format style.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of an Objective-C subclass to a
string interpolation.

`func appendInterpolation<Subject>(Subject, formatter: Formatter?)`

Appends an optionally-formatted instance of a Foundation type to a string
interpolation.

`func appendInterpolation(Date, style: Text.DateStyle)`

Appends a formatted date to a string interpolation.

`func appendInterpolation(Text)`

Appends the string displayed by a text view to a string interpolation.

`func appendInterpolation(Image)`

Appends an image to a string interpolation.

`func appendInterpolation(LocalizedStringResource)`

Appends the localized string resource to a string interpolation.

`func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date?,
countsDown: Bool, showsHours: Bool)`

Appends a timer interval to a string interpolation.


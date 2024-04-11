# LocalizedStringKey.StringInterpolation

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



# Label

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a localized
string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image name: String
    )

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`titleKey`

    

A title generated from a localized string.

`image`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an image

`init<S>(S, image: String)`

Creates a label with an icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image name: String
    ) where S : StringProtocol

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`title`

    

A string used as the label’s title.

`image`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an image

`init(LocalizedStringKey, image: String)`

Creates a label with an icon image and a title generated from a localized
string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:systemImage:)

Creates a label with a system icon image and a title generated from a
localized string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        systemImage name: String
    )

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`titleKey`

    

A title generated from a localized string.

`systemImage`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an SF Symbol

`init<S>(S, systemImage: String)`

Creates a label with a system icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:systemImage:)

Creates a label with a system icon image and a title generated from a string.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        systemImage name: String
    ) where S : StringProtocol

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`title`

    

A string used as the label’s title.

`systemImage`

    

The name of the image resource to lookup.

## See Also

### Creating a label from text and an SF Symbol

`init(LocalizedStringKey, systemImage: String)`

Creates a label with a system icon image and a title generated from a
localized string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(title:icon:)

Creates a label with a custom title and icon.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder title: () -> Title,
        @ViewBuilder icon: () -> Icon
    )

Initializer

# init(_:)

Creates a label representing the configuration of a style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(_ configuration: LabelStyleConfiguration)

Available when `Title` is `LabelStyleConfiguration.Title` and `Icon` is
`LabelStyleConfiguration.Icon`.

##  Parameters

`configuration`

    

The label style to use.

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`LabelStyle` instance to create an instance of the label that’s being styled.
This is useful for custom label styles that only wish to modify the current
style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the label, but
otherwise preserves the current style:

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a localized
string.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        image resource: ImageResource
    )

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`titleKey`

    

A title generated from a localized string.

`image`

    

The image resource to lookup.

## See Also

### Creating a label from an image resource

`init<S>(S, image: ImageResource)`

Creates a label with an icon image and a title generated from a string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:image:)

Creates a label with an icon image and a title generated from a string.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        image resource: ImageResource
    ) where S : StringProtocol

Available when `Title` is `Text` and `Icon` is `Image`.

##  Parameters

`title`

    

A string used as the label’s title.

`image`

    

The image resource to lookup.

## See Also

### Creating a label from an image resource

`init(LocalizedStringKey, image: ImageResource)`

Creates a label with an icon image and a title generated from a localized
string.

Available when `Title` is `Text` and `Icon` is `Image`.

Initializer

# init(_:)

Creates a label representing a family activity application.

iOS 15.2+  iPadOS 15.2+  Mac Catalyst 15.2+  visionOS 1.0+

    
    
    init(_ applicationToken: ApplicationToken)

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## See Also

### Creating a family activity label

`init(WebDomainToken)`

Creates a label representing a family activity web domain.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(ActivityCategoryToken)`

Creates a label representing a family activity category.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

Initializer

# init(_:)

Creates a label representing a family activity web domain.

iOS 15.2+  iPadOS 15.2+  Mac Catalyst 15.2+  visionOS 1.0+

    
    
    init(_ webDomainToken: WebDomainToken)

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## See Also

### Creating a family activity label

`init(ApplicationToken)`

Creates a label representing a family activity application.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(ActivityCategoryToken)`

Creates a label representing a family activity category.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

Initializer

# init(_:)

Creates a label representing a family activity category.

iOS 15.2+  iPadOS 15.2+  Mac Catalyst 15.2+  visionOS 1.0+

    
    
    init(_ categoryToken: ActivityCategoryToken)

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

## See Also

### Creating a family activity label

`init(ApplicationToken)`

Creates a label representing a family activity application.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.

`init(WebDomainToken)`

Creates a label representing a family activity web domain.

Available when `Title` is `FamilyActivityTitleView` and `Icon` is
`FamilyActivityIconView`.



# LazyVGrid

Initializer

# init(columns:alignment:spacing:pinnedViews:content:)

Creates a grid that grows vertically.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        columns: [GridItem],
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil,
        pinnedViews: PinnedScrollableViews = .init(),
        @ViewBuilder content: () -> Content
    )

##  Parameters

`columns`

    

An array of grid items to size and position each row of the grid.

`alignment`

    

The alignment of the grid within its parent view.

`spacing`

    

The spacing between the grid and the next item in its parent view.

`pinnedViews`

    

Views to pin to the bounds of a parent scroll view.

`content`

    

The content of the grid.



# LayoutDirectionBehavior

Case

# LayoutDirectionBehavior.fixed

A behavior that doesn’t mirror when the layout direction changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case fixed

## See Also

### Getting behaviors

`static var mirrors: LayoutDirectionBehavior`

A behavior that mirrors when the layout direction is right-to-left.

`case mirrors(in: LayoutDirection)`

A behavior that mirrors when the layout direction has the specified value.

Type Property

# mirrors

A behavior that mirrors when the layout direction is right-to-left.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    static var mirrors: LayoutDirectionBehavior { get }

## See Also

### Getting behaviors

`case fixed`

A behavior that doesn’t mirror when the layout direction changes.

`case mirrors(in: LayoutDirection)`

A behavior that mirrors when the layout direction has the specified value.

Case

# LayoutDirectionBehavior.mirrors(in:)

A behavior that mirrors when the layout direction has the specified value.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    case mirrors(in: LayoutDirection)

## Discussion

If you develop your view or shape in an LTR context, you can use `.mirrors(in:
.rightToLeft)` (which is equivalent to `.mirrors`) to mirror your content when
the layout direction is RTL (and keep the original version in LTR). If you
developer in an RTL context, you can use `.mirrors(in: .leftToRight)` to
mirror your content when the layout direction is LTR (and keep the original
version in RTL).

## See Also

### Getting behaviors

`case fixed`

A behavior that doesn’t mirror when the layout direction changes.

`static var mirrors: LayoutDirectionBehavior`

A behavior that mirrors when the layout direction is right-to-left.



# LocalizedStringKey

Initializer

# init(_:)

Creates a localized string key from the given string value.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(_ value: String)

##  Parameters

`value`

    

The string to use as a localization key.

## See Also

### Creating a key from a literal value

`init(stringLiteral: String)`

Creates a localized string key from the given string literal.

Initializer

# init(stringLiteral:)

Creates a localized string key from the given string literal.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(stringLiteral value: String)

##  Parameters

`value`

    

The string literal to use as a localization key.

## See Also

### Creating a key from a literal value

`init(String)`

Creates a localized string key from the given string value.

Initializer

# init(stringInterpolation:)

Creates a localized string key from the given string interpolation.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(stringInterpolation: LocalizedStringKey.StringInterpolation)

##  Parameters

`stringInterpolation`

    

The string interpolation to use as the localization key.

## Discussion

To create a localized string key from a string interpolation, use the `\()`
string interpolation syntax. Swift matches the parameter types in the
expression to one of the `appendInterpolation` methods in
`LocalizedStringKey.StringInterpolation`. The interpolated types can include
numeric values, Foundation types, and SwiftUI `Text` and `Image` instances.

The following example uses a string interpolation with two arguments: an
unlabeled `Date` and a `Text.DateStyle` labeled `style`. The compiler maps
these to the method `appendInterpolation(_:style:)` as it builds the string
that it creates the `LocalizedStringKey` with.

You can write this example more concisely, implicitly creating a
`LocalizedStringKey` as the parameter to the `Text` initializer:

## See Also

### Creating a key from an interpolation

`struct StringInterpolation`

Represents the contents of a string literal with interpolations while it’s
being built, for use in creating a localized string key.

Structure

# LocalizedStringKey.StringInterpolation

Represents the contents of a string literal with interpolations while it’s
being built, for use in creating a localized string key.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct StringInterpolation

## Topics

### Appending to an interpolation

The compiler uses these methods when interpreting string interpolations; don’t
call them directly.

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

`func appendLiteral(String)`

Appends a literal string.

## Relationships

### Conforms To

  * `StringInterpolationProtocol`

## See Also

### Creating a key from an interpolation

`init(stringInterpolation: LocalizedStringKey.StringInterpolation)`

Creates a localized string key from the given string interpolation.



# LayoutSubviews

Instance Property

# layoutDirection

The layout direction inherited by the container view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var layoutDirection: LayoutDirection

## Discussion

SwiftUI supports both left-to-right and right-to-left directions. Read this
property within a custom layout container to find out which environment the
container is in.

In most cases, you don’t need to take any action based on this value. SwiftUI
horizontally flips the x position of each view within its parent when the mode
switches, so layout calculations automatically produce the desired effect for
both directions.

Instance Subscript

# subscript(_:)

Gets the subview proxy at a specified index.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript(index: Int) -> LayoutSubviews.Element { get }

## See Also

### Accessing subviews

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Subscript

# subscript(_:)

Gets the subview proxies with the specified indicies.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<S>(indices: S) -> LayoutSubviews where S : Sequence, S.Element == Int { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Subscript

# subscript(_:)

Gets the subview proxies in the specified range.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript(bounds: Range<Int>) -> LayoutSubviews { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Property

# startIndex

The index of the first subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var startIndex: Int { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Instance Property

# endIndex

An index that’s one higher than the last subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var endIndex: Int { get }

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Type Alias

# LayoutSubviews.Element

A type that contains a proxy value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Element = LayoutSubview

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Index`

A type that you can use to index proxy values.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Type Alias

# LayoutSubviews.Index

A type that you can use to index proxy values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Index = Int

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias SubSequence`

A type that contains a subsequence of proxy values.

Type Alias

# LayoutSubviews.SubSequence

A type that contains a subsequence of proxy values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias SubSequence = LayoutSubviews

## See Also

### Accessing subviews

`subscript(Int) -> LayoutSubviews.Element`

Gets the subview proxy at a specified index.

`subscript<S>(S) -> LayoutSubviews`

Gets the subview proxies with the specified indicies.

`subscript(Range<Int>) -> LayoutSubviews`

Gets the subview proxies in the specified range.

`var startIndex: Int`

The index of the first subview.

`var endIndex: Int`

An index that’s one higher than the last subview.

`typealias Element`

A type that contains a proxy value.

`typealias Index`

A type that you can use to index proxy values.



# LinkButtonStyle

Initializer

# init()

Creates a link button style.

macOS 10.15+

    
    
    init()

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a button.

macOS 10.15+

    
    
    func makeBody(configuration: LinkButtonStyle.Configuration) -> some View
    

##  Parameters

`configuration`

    

The properties of the button.

## Discussion

The system calls this method for each `Button` instance in a view hierarchy
where this style is the current button style.



# LinearGaugeStyle

Initializer

# init()

Creates a linear gauge style.

watchOS 7.0+

    
    
    init()

Initializer

# init(tint:)

Creates a linear gauge style with a tint color.

watchOS 7.0–10.4  Deprecated

    
    
    init(tint: Color)

Deprecated

Use the `tint(_:)` view modifier instead.

## See Also

### Deprecated initializers

`init(tint: Gradient)`

Creates a linear gauge style with a tint gradient.

Deprecated

Initializer

# init(tint:)

Creates a linear gauge style with a tint gradient.

watchOS 7.0–10.4  Deprecated

    
    
    init(tint: Gradient)

Deprecated

Use the `tint(_:)` view modifier instead.

## See Also

### Deprecated initializers

`init(tint: Color)`

Creates a linear gauge style with a tint color.

Deprecated



# LabeledContentStyle

Type Property

# automatic

A labeled content style that resolves its appearance automatically based on
the current context.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var automatic: AutomaticLabeledContentStyle { get }

Available when `Self` is `AutomaticLabeledContentStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of labeled content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

## See Also

### Creating custom labeled content styles

`typealias Configuration`

The properties of a labeled content instance.

`associatedtype Body : View`

A view that represents the appearance and behavior of labeled content.

**Required**

Type Alias

# LabeledContentStyle.Configuration

The properties of a labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Configuration = LabeledContentStyleConfiguration

## See Also

### Creating custom labeled content styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of labeled content.

**Required**

` associatedtype Body : View`

A view that represents the appearance and behavior of labeled content.

**Required**

Associated Type

# Body

A view that represents the appearance and behavior of labeled content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom labeled content styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of labeled content.

**Required**

` typealias Configuration`

The properties of a labeled content instance.

Structure

# AutomaticLabeledContentStyle

The default labeled content style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct AutomaticLabeledContentStyle

## Overview

Use `automatic` to construct this style.

## Topics

### Creating the labeled content style

`init()`

Creates an automatic labeled content style.

## Relationships

### Conforms To

  * `LabeledContentStyle`



# LazyHGrid

Initializer

# init(rows:alignment:spacing:pinnedViews:content:)

Creates a grid that grows horizontally.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        rows: [GridItem],
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        pinnedViews: PinnedScrollableViews = .init(),
        @ViewBuilder content: () -> Content
    )

##  Parameters

`rows`

    

An array of grid items that size and position each column of the grid.

`alignment`

    

The alignment of the grid within its parent view.

`spacing`

    

The spacing between the grid and the next item in its parent view.

`pinnedViews`

    

Views to pin to the bounds of a parent scroll view.

`content`

    

The content of the grid.



# LabeledContentStyleConfiguration

Instance Property

# label

The label of the labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let label: LabeledContentStyleConfiguration.Label

## See Also

### Configuring the label

`struct Label`

A type-erased label of a labeled content instance.

Structure

# LabeledContentStyleConfiguration.Label

A type-erased label of a labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Label

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the label

`let label: LabeledContentStyleConfiguration.Label`

The label of the labeled content instance.

Instance Property

# content

The content of the labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    let content: LabeledContentStyleConfiguration.Content

## See Also

### Configuring the content

`struct Content`

A type-erased content of a labeled content instance.

Structure

# LabeledContentStyleConfiguration.Content

A type-erased content of a labeled content instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Content

## Relationships

### Conforms To

  * `View`

## See Also

### Configuring the content

`let content: LabeledContentStyleConfiguration.Content`

The content of the labeled content instance.



# ListItemTint

Type Property

# monochrome

A standard grayscale tint effect.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static let monochrome: ListItemTint

## Discussion

The system doesn’t override monochrome tints.

## See Also

### Getting list item tint options

`static func fixed(Color) -> ListItemTint`

An explicit tint color.

`static func preferred(Color) -> ListItemTint`

An explicit tint color that the system can override.

Type Method

# fixed(_:)

An explicit tint color.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func fixed(_ tint: Color) -> ListItemTint

##  Parameters

`tint`

    

The color to use to tint the content.

## Discussion

The system doesn’t override this tint effect.

## See Also

### Getting list item tint options

`static let monochrome: ListItemTint`

A standard grayscale tint effect.

`static func preferred(Color) -> ListItemTint`

An explicit tint color that the system can override.

Type Method

# preferred(_:)

An explicit tint color that the system can override.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static func preferred(_ tint: Color) -> ListItemTint

##  Parameters

`tint`

    

The color to use to tint the content.

## Discussion

The system can override this tint effect, like when the system has a custom
user accent color on macOS.

## See Also

### Getting list item tint options

`static let monochrome: ListItemTint`

A standard grayscale tint effect.

`static func fixed(Color) -> ListItemTint`

An explicit tint color.



# Layout adjustments

Article

# Laying out a simple view

Create a view layout by adjusting the size of views.

## Overview

To create a layout for a view, start by composing a hierarchy of child views.
Then, refine the size and spacing of the child views with configuration
parameters, and by adding view modifiers, like those that affect a view’s
frame and padding. To review how to compose layouts, see Building layouts with
stack views.

### Establish a view hierarchy

The following example creates a view to display an incoming message from a
messaging service. The view uses an `HStack` to collect a view that identifies
the sender and another that provides the content of the message:

The following screenshot of a `MessageRow` view includes a border that shows
its bounds. Note the large size of the circle, which fills the space available
to it:

When SwiftUI renders a view hierarchy, it recursively evaluates each child
view: The parent view proposes a size to the child views it contains, and the
child views respond with a computed size.

The `MessageRow` view proposes a size to its only child, the `HStack`, which
is the full size proposed to it by its own parent. The stack proportionally
divides this space between its child views, with system-default spacing
between each child. This continues recursively:

  * The `ZStack` proposes a size to its child views, the `Circle` and `Text` views.

  * The `Circle` expands up to the size offered, while the `Text` takes just enough space for the string it contains.

  * The `ZStack` returns the size of its largest child view, in this case the `Circle`.

When all child views have reported their size, the parent view renders them.
For a hands-on approach to learning how the SwiftUI view hierarchy works, see
the Building lists and navigation section in the Introducing SwiftUI tutorial.

### Limit the view size

In the example above, SwiftUI has built-in views that manage size in different
ways, including views that:

  * Expand to fill the space offered by their parent, like `Color`, `LinearGradient`, and `Circle`.

  * Have an ideal size that varies according to their contents, like `Text` and the container views.

  * Have an ideal size that never varies, like `Toggle` or `DatePicker`.

You can constrain a view to a fixed size by adding a frame modifier. For
example, use the `frame(width:height:alignment:)` modifier to limit the width
the circle to `40` points:

When you add a frame modifier, SwiftUI wraps the affected view, effectively
adding a new view to the view hierarchy.

When SwiftUI evaluates this new hierarchy, the frame modifier fixes the width
of the `ZStack` that it wraps by passing along the value you specified as its
parameter. The remainder of the size evaluation proceeds as before, where the
`Circle` now expands to fill a smaller space, constrained by the frame’s 40
point width. This enables the `HStack` to provide more space to its other
child, which displays the message text.

### Position content with alignment

If you want the top of the circle aligned with the top of the message content
text, you can refine the view by applying an alignment to the `HStack`. To
position the content vertically within the stack, specify the `alignment`
parameter to `top`:

With the alignment applied, you get an unexpected result. The tops of the
views don’t appear to align:

However, if you select the circle in Xcode, or temporarily add a border to the
circle, you can see the tops of the views do in fact align. For more
information on inspecting the size of a view, see Inspecting view layout.

In the previous section, you applied a frame with only a width constraint.
SwiftUI drew a circle limited by that width. But because the height was left
unspecified, the circle’s frame separately expanded to fill the available
height, even though that extra space had no visible impact on the rendered
circle. You can resolve this problem by adding an explicit `height` parameter:

The contents of the `HStack` are now top aligned, although the stack itself is
centered in the `MessageRow` view as shown by the border displaying the row’s
boundaries.

### Add padding to the view

To avoid visually crowding the outer edges of a view, add padding. This
introduces a fixed amount of space along the specified edges, reducing the
space available for the contents of the view by a corresponding amount. For
example, you can use `padding(_:_:)` to add extra space along the `horizontal`
edges of the `HStack`:

The padding modifier defaults to system-standard spacing, although you can
alternatively choose different values for the padding modifier.

## See Also

### Finetuning a layout

Inspecting view layout

Determine the position and extent of a view using Xcode previews or by adding
temporary borders.

Article

# Inspecting view layout

Determine the position and extent of a view using Xcode previews or by adding
temporary borders.

## Overview

To learn how SwiftUI sizes and positions views, take advantage of Xcode
previews to inspect a single view’s boundaries. You can also add temporary
borders to see how SwiftUI positions and sizes multiple views together.

### Highlight views with Xcode previews

Using Xcode previews, you can quickly see the size of a specific view element
by selecting the view or child view in the editor. To illustrate this, the
following example uses a `VStack` to vertically group an image, provided by SF
Symbols, above a name:

With the `VStack` selected, you’ll see a blue border around the view in the
Xcode preview:

### Use temporary borders to explore complex layouts

To see the border of more than one view, or to see a border when the view
isn’t selected, temporarily add a border with the view modifier
`border(_:width:)`. Set the border’s color to something other than `blue` to
easily distinguish it from a border added by Xcode:

## See Also

### Finetuning a layout

Laying out a simple view

Create a view layout by adjusting the size of views.

Instance Method

# padding(_:)

Adds a specific padding amount to each edge of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(_ length: CGFloat) -> some View
    

##  Parameters

`length`

    

The amount, given in points, to pad this view on all edges.

## Return Value

A view that’s padded by the amount you specify.

## Discussion

Use this modifier to add padding all the way around a view.

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

To independently control the amount of padding for each edge, use
`padding(_:)`. To pad a select set of edges by the same amount, use
`padding(_:_:)`.

## See Also

### Adding padding around a view

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding(_:_:)

Adds an equal padding amount to specific edges of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(
        _ edges: Edge.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

##  Parameters

`edges`

    

The set of edges to pad for this view. The default is `all`.

`length`

    

An amount, given in points, to pad this view on the specified edges. If you
set the value to `nil`, SwiftUI uses a platform-specific default amount. The
default value of this parameter is `nil`.

## Return Value

A view that’s padded by the specified amount on the specified edges.

## Discussion

Use this modifier to add a specified amount of padding to one or more edges of
the view. Indicate the edges to pad by naming either a single value from
`Edge.Set`, or by specifying an `OptionSet` that contains edge values:

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

You can omit either or both of the parameters. If you omit the `length`,
SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI
applies the padding to all edges. Omit both to add a default padding all the
way around a view. SwiftUI chooses a default amount of padding that’s
appropriate for the platform and the presentation context.

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use
`padding(_:)`. To pad all outside edges of a view by a specified amount, use
`padding(_:)`.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding(_:)

Adds a different padding amount to each edge of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(_ insets: EdgeInsets) -> some View
    

##  Parameters

`insets`

    

An `EdgeInsets` instance that contains padding amounts for each edge.

## Return Value

A view that’s padded by different amounts on each edge.

## Discussion

Use this modifier to add a different amount of padding on each edge of a view:

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

To pad a view on specific edges with equal padding for all padded edges, use
`padding(_:_:)`. To pad all edges of a view equally, use `padding(_:)`.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:)

Pads this view along all edge insets by the amount you specify.

visionOS 1.0+

    
    
    func padding3D(_ length: CGFloat) -> some View
    

##  Parameters

`length`

    

The amount to inset this view on each edge.

## Return Value

A view that pads this view by the amount you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:)

Pads this view using the edge insets you specify.

visionOS 1.0+

    
    
    func padding3D(_ insets: EdgeInsets3D) -> some View
    

##  Parameters

`insets`

    

The edges to inset.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:_:)

Pads this view using the edge insets you specify.

visionOS 1.0+

    
    
    func padding3D(
        _ edges: Edge3D.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

##  Parameters

`edges`

    

The set of edges along which to inset this view.

`length`

    

The amount to inset this view on each edge. If `nil`, the amount is the system
default amount.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# scenePadding(_:)

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func scenePadding(_ edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view.
Specify either a single edge value from `Edge.Set`, or an `OptionSet` that
describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root
view of a window. In watchOS, use scene padding to align elements of your user
interface with top level elements, like the title of a navigation view. For
example, compare the effects of different kinds of padding on text views
presented inside a `NavigationView` in watchOS:

The text with scene padding automatically aligns with the title, unlike the
text that uses the default padding or the text without padding:

Scene padding in watchOS also ensures that your content avoids the curved
edges of a device like Apple Watch Series 7. In other platforms, scene padding
produces the same default padding that you get from the `padding(_:_:)`
modifier.

Important

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even
if you specify those edges as part of the input. For example, if you specify
`vertical` instead of `horizontal` in the example above, the modifier would
have no effect in watchOS. It does, however, apply to all the edges that you
specify in other platforms.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# scenePadding(_:edges:)

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scenePadding(
        _ padding: ScenePadding,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`padding`

    

The kind of padding to add.

`edges`

    

The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view.
Specify either a single edge value from `Edge.Set`, or an `OptionSet` that
describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root
view of a window. In watchOS, use scene padding to align elements of your user
interface with top level elements, like the title of a navigation view. For
example, compare the effects of different kinds of padding on text views
presented inside a `NavigationView` in watchOS:

The text with minimum scene padding uses the system minimum padding and the
text with navigation bar scene padding automatically aligns with the
navigation bar content. In contrast, the text that uses the default padding
and the text without padding do not align with scene elements.

Scene padding in watchOS also ensures that your content avoids the curved
edges of a device like Apple Watch Series 7. In other platforms, scene padding
produces the same default padding that you get from the `padding(_:_:)`
modifier.

Important

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even
if you specify those edges as part of the input. For example, if you specify
`vertical` instead of `horizontal` in the example above, the modifier would
have no effect in watchOS. It does, however, apply to all the edges that you
specify in other platforms.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Structure

# ScenePadding

The padding used to space a view from its containing scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct ScenePadding

## Overview

Add scene padding to a view using the `scenePadding(_:edges:)` modifier.

## Topics

### Getting padding values

`static let minimum: ScenePadding`

The minimum scene padding value.

`static let navigationBar: ScenePadding`

The navigation bar content scene padding.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

Instance Method

# frame(width:height:alignment:)

Positions this view within an invisible frame with the specified size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame(
        width: CGFloat? = nil,
        height: CGFloat? = nil,
        alignment: Alignment = .center
    ) -> some View
    

##  Parameters

`width`

    

A fixed width for the resulting view. If `width` is `nil`, the resulting view
assumes this view’s sizing behavior.

`height`

    

A fixed height for the resulting view. If `height` is `nil`, the resulting
view assumes this view’s sizing behavior.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with fixed dimensions of `width` and `height`, for the parameters that
are non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s width, height, or both.
If you only specify one of the dimensions, the resulting view assumes this
view’s sizing behavior in the other dimension.

For example, the following code lays out an ellipse in a fixed 200 by 100
frame. Because a shape always occupies the space offered to it by the layout
system, the first ellipse is 200x100 points. The second ellipse is laid out in
a frame with only a fixed height, so it occupies that height, and whatever
width the layout system offers to its parent.

`The alignment` parameter specifies this view’s alignment within the frame.

In the example above, the text is positioned at the top, leading corner of the
frame. If the text is taller than the frame, its bounds may extend beyond the
bottom of the frame’s bounds.

## See Also

### Influencing a view’s size

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# frame(depth:alignment:)

Positions this view within an invisible frame with the specified depth.

visionOS 1.0+

    
    
    func frame(
        depth: CGFloat?,
        alignment: DepthAlignment = .center
    ) -> some View
    

##  Parameters

`depth`

    

A fixed depth for the resulting view. If `depth` is `nil`, the resulting view
assumes this view’s sizing behavior.

`alignment`

    

The alignment of this view inside the resulting view. `alignment` applies if
this view is smaller than the size given by the resulting frame.

## Return Value

A view with a fixed dimension of `depth` if non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s depth. If you don’t
specify a dimension, the resulting view assumes this view’s sizing behavior in
depth.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

#
frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)

Positions this view within an invisible frame having the specified size
constraints.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame(
        minWidth: CGFloat? = nil,
        idealWidth: CGFloat? = nil,
        maxWidth: CGFloat? = nil,
        minHeight: CGFloat? = nil,
        idealHeight: CGFloat? = nil,
        maxHeight: CGFloat? = nil,
        alignment: Alignment = .center
    ) -> some View
    

##  Parameters

`minWidth`

    

The minimum width of the resulting frame.

`idealWidth`

    

The ideal width of the resulting frame.

`maxWidth`

    

The maximum width of the resulting frame.

`minHeight`

    

The minimum height of the resulting frame.

`idealHeight`

    

The ideal height of the resulting frame.

`maxHeight`

    

The maximum height of the resulting frame.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass
`nil` or leave out a characteristic to indicate that the frame should adopt
this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by
any constraints specified, and with any ideal dimensions specified replacing
any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the
frame adopts the sizing behavior of its child in that dimension. If both
constraints are specified in a dimension, the frame unconditionally adopts the
size proposed for it, clamped to the constraints. Otherwise, the size of the
frame in either dimension is:

  * If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.

  * If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.

  * Otherwise, the size of this view.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# frame(minDepth:idealDepth:maxDepth:alignment:)

Positions this view within an invisible frame having the specified depth
constraints.

visionOS 1.0+

    
    
    func frame(
        minDepth: CGFloat? = nil,
        idealDepth: CGFloat? = nil,
        maxDepth: CGFloat? = nil,
        alignment: DepthAlignment = .center
    ) -> some View
    

##  Parameters

`minDepth`

    

The minimum depth of the resulting frame.

`idealDepth`

    

The ideal depth of the resulting frame.

`maxDepth`

    

The maximum depth of the resulting frame.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass
`nil` or leave out a characteristic to indicate that the frame should adopt
this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by
any constraints specified, and with an ideal dimension specified replacing any
corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the
frame adopts the sizing behavior of its child in that dimension. If both
constraints are specified in a dimension, the frame unconditionally adopts the
size proposed for it, clamped to the constraints. Otherwise, the size of the
frame in either dimension is:

  * If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.

  * If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.

  * Otherwise, the size of this view.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:alignment:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        alignment: Alignment = .center
    ) -> some View
    

## Discussion

Use this modifier to specify a size for a view’s width, height, or both that
is dependent on the size of the nearest container. Different things can
represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use the `containerRelativeFrame(_:count:span:spacing:alignment:)` modifier to
size a view such that multiple views will be visible in the container. When
using this modifier, the count refers to the total number of rows or columns
that the length of the container size in a particular axis should be divided
into. The span refers to the number of rows or columns that the modified view
should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use the `containerRelativeFrame(_:alignment:_:)` modifier to apply your own
custom logic to adjust the size of the nearest container for your view. The
following example will result in the container frame’s width being divided by
3 and using that value as the width of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:alignment:_:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        alignment: Alignment = .center,
        _ length: @escaping (CGFloat, Axis) -> CGFloat
    ) -> some View
    

## Discussion

Use the `containerRelativeFrame(_:alignment:)` modifier to specify a size for
a view’s width, height, or both that is dependent on the size of the nearest
container. Different things can represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use the `View/containerRelativeFrame(_:count:spacing:alignment:)` modifier to
size a view such that multiple views will be visible in the container. When
using this modifier, the count refers to the total number of rows or columns
that the length of the container size in a particular axis should be divided
into. The span refers to the number of rows or columns that the modified view
should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use this modifier to apply your own custom logic to adjust the size of the
nearest container for your view. The following example will result in the
container frame’s width being divided by 3 and using that value as the width
of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:count:span:spacing:alignment:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        count: Int,
        span: Int = 1,
        spacing: CGFloat,
        alignment: Alignment = .center
    ) -> some View
    

## Discussion

Use the `containerRelativeFrame(_:alignment:)` modifier to specify a size for
a view’s width, height, or both that is dependent on the size of the nearest
container. Different things can represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use this modifier to size a view such that multiple views will be visible in
the container. When using this modifier, the count refers to the total number
of rows or columns that the length of the container size in a particular axis
should be divided into. The span refers to the number of rows or columns that
the modified view should actually occupy. Thus the size of the element can be
described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use the `containerRelativeFrame(_:alignment:_:)` modifier to apply your own
custom logic to adjust the size of the nearest container for your view. The
following example will result in the container frame’s width being divided by
3 and using that value as the width of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# fixedSize()

Fixes this view at its ideal size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fixedSize() -> some View
    

## Return Value

A view that fixes this view at its ideal size.

## Discussion

During the layout of the view hierarchy, each view proposes a size to each
child view it contains. If the child view doesn’t need a fixed size it can
accept and conform to the size offered by the parent.

For example, a `Text` view placed in an explicitly sized frame wraps and
truncates its string to remain within its parent’s bounds:

The `fixedSize()` modifier can be used to create a view that maintains the
_ideal size_ of its children both dimensions:

This can result in the view exceeding the parent’s bounds, which may or may
not be the effect you want.

You can think of `fixedSize()` as the creation of a _counter proposal_ to the
view size proposed to a view by its parent. The ideal size of a view, and the
specific effects of `fixedSize()` depends on the particular view and how you
have configured it.

To create a view that fixes the view’s size in either the horizontal or
vertical dimensions, see `fixedSize(horizontal:vertical:)`.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# fixedSize(horizontal:vertical:)

Fixes this view at its ideal size in the specified dimensions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fixedSize(
        horizontal: Bool,
        vertical: Bool
    ) -> some View
    

##  Parameters

`horizontal`

    

A Boolean value that indicates whether to fix the width of the view.

`vertical`

    

A Boolean value that indicates whether to fix the height of the view.

## Return Value

A view that fixes this view at its ideal size in the dimensions specified by
`horizontal` and `vertical`.

## Discussion

This function behaves like `fixedSize()`, except with
`fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally
specified in one or both dimensions. For example, if you horizontally fix a
text view before wrapping it in the frame view, you’re telling the text view
to maintain its ideal _width_. The view calculates this to be the space needed
to represent the entire string.

This can result in the view exceeding the parent’s bounds, which may or may
not be the effect you want.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# layoutPriority(_:)

Sets the priority by which a parent layout should apportion space to this
child.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func layoutPriority(_ value: Double) -> some View
    

##  Parameters

`value`

    

The priority by which a parent layout apportions space to the child.

## Discussion

Views typically have a default priority of `0` which causes space to be
apportioned evenly to all sibling views. Raising a view’s layout priority
encourages the higher priority view to shrink later when the group is shrunk
and stretch sooner when the group is stretched.

In the example above, the first `Text` element has the default priority `0`
which causes its view to shrink dramatically due to the higher priority of the
second `Text` element, even though all of their other attributes (font, font
size and character count) are the same.

A parent layout offers the child views with the highest layout priority all
the space offered to the parent minus the minimum space required for all its
lower-priority children.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

Article

# Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

## Overview

Use SwiftUI to adaptively lay out and position your views. If you can’t
achieve your design with composition alone, fine tune the layout with view
modifiers. Add an offset modifier to shift the rendered content of a view from
its current position, or a position modifier to set an explicit position
within its parent.

### Create a view layout

The following example provides a view to illustrate how to position views,
providing a rough layout of views composed within a `ZStack`. The stack
contains a quadrant with an overlaid circle image:

For more detail on composing views with stacks, see Building layouts with
stack views.

### Shift the location of a view’s content

Fine-tune the position of the circle within the quadrant by using an offset
modifier to shift where the parent view places the circle. An offset modifier
shifts the image from its default center position. For example, the
`offset(x:y:)` modifier uses the parameters of `x` and `y` to represent a
relative location within the view’s coordinate space.

In SwiftUI, the view’s coordinate space uses `x` to represent a horizontal
direction and `y` to represent a vertical direction. The value of `x` starts
at `0` at the leading edge of a view, and increases as the location moves
toward the trailing edge of a view. The value of `y` starts at `0` at the top
edge of a view, and increases as the location moves toward the bottom edge of
a view. Don’t assume the leading edge is always on the left, because it
changes with the layout direction. When the layout direction is set to right-
to-left, the `0` horizontal value is on the right side of the view.

The following diagram shows the coordinates in the left-to-right layout
direction against a rectangle, with the origin at the top, leading corner:

The following example shifts the circle `40` points from the center, up and
toward the trailing edge:

### Position view content explicitly

To explicitly position elements within a view, use the `position(x:y:)` view
modifier. A position modifier overrides where the parent view places its
content. The modifier renders the view at a location offset from the origin of
the parent view, unlike an offset modifier that shifts the view from the
location chosen by the parent view. The position modifier uses the same `x`,
`y` coordinate system as the offset modifier, and similarly doesn’t influence
the size of the view. In this example, the position of the circle is set
halfway down on the right side of the quadrant with explicit values:

## See Also

### Adjusting a view’s position

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# position(_:)

Positions the center of this view at the specified point in its parent’s
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func position(_ position: CGPoint) -> some View
    

##  Parameters

`position`

    

The point at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `position`.

## Discussion

Use the `position(_:)` modifier to place the center of a view at a specific
coordinate in the parent view using a `CGPoint` to specify the `x` and `y`
offset.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# position(x:y:)

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func position(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`x`

    

The x-coordinate at which to place the center of this view.

`y`

    

The y-coordinate at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `x` and `y`.

## Discussion

Use the `position(x:y:)` modifier to place the center of a view at a specific
coordinate in the parent view using an `x` and `y` offset.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(_:)

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGSize) -> some View
    

##  Parameters

`offset`

    

The distance to offset this view.

## Return Value

A view that offsets this view by `offset`.

## Discussion

Use `offset(_:)` to shift the displayed contents by the amount specified in
the `offset` parameter.

The original dimensions of the view aren’t changed by offsetting the contents;
in the example below the gray border drawn by this view surrounds the original
position of the text:

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(x:y:)

Offset this view by the specified horizontal and vertical distances.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`x`

    

The horizontal distance to offset this view.

`y`

    

The vertical distance to offset this view.

## Return Value

A view that offsets this view by `x` and `y`.

## Discussion

Use `offset(x:y:)` to shift the displayed contents by the amount specified in
the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents;
in the example below the gray border drawn by this view surrounds the original
position of the text:

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(z:)

Brings a view forward in Z by the provided distance in points.

visionOS 1.0+

    
    
    func offset(z: CGFloat) -> some View
    

##  Parameters

`distance`

    

The distance to extrude the view forward in Z, in points.

## Return Value

A view that is extruded forward in Z by `distance`.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

Article

# Aligning views within a stack

Position views inside a stack using alignment guides.

## Overview

Stacks place their child views to match their alignment, which defaults to
center alignment. When you initialize the stack, you can specify an alignment
for the stack to use that also applies to a stack’s child views. If you want
to modify the placement of individual child views, use the alignment guide
modifier to make adjustments that offset the view from the alignment the stack
provides.

To align views across multiple stacks, see Aligning views across stacks.

### Use defaults for basic alignment

For an example of how SwiftUI applies default alignment to the views in an
`HStack`, examine the following code used to provide a status view for a
recording app. The `HStack` contains an image view for the icon and two text
views with labels that use the `font(_:)` modifier to adjust the font size of
the text.

The orange reference line in the following figure shows the default alignment
position of the views within the stack. The line functions as a visual
reference for the purposes of this article.

### Customize stack alignment

You can align content within a stack based on guides provided by the
alignments that the stack supports. The various kinds of stacks support the
following alignments:

  * `HStack` uses the guides defined in `VerticalAlignment`.

  * `VStack` uses the guides defined in `HorizontalAlignment`.

  * `ZStack` uses the guides defined in `Alignment`, and a combination of `HorizontalAlignment` and `VerticalAlignment`.

Use the `alignment` parameter when initializing a stack to define the
alignment guide for the stack. The following example sets the alignment of the
`HStack` to `firstTextBaseline`, which aligns its child views to the baseline
of the first text view (which contains the string “Connecting”):

### Adjust the alignment of individual views within a stack

Custom images don’t provide a text baseline guide, so the bottom of the image
aligns to the text view’s baseline. Adjust the alignment of the image using
`alignmentGuide(_:computeValue:)` to get the visual alignment you desire. The
alignment guide’s closure provides an instance of `ViewDimensions`, the
parameter `context` in this example — which you can use to return an offset
value. The value looked up from `context` with `bottom`, provides an offset
that aligns the bottom of the image adjusted by an offset to the baseline
guide defined on the stack:

When you use an alignment guide modifier, make sure to specify an active
alignment of the stack. Otherwise, SwiftUI doesn’t invoke the closure to
offset the view. In the example above, the `firstTextBaseline` input to the
alignment guide matches the stack’s alignment, so the adjustment affects the
placement of the image:

### Use SF Symbols to simplify views when aligning with text

You can replace the microphone image with a similar icon from SF Symbols to
simplify the view. The icons from SF Symbols use text baseline guides, which
means they support whatever font styling you apply to the view.

## See Also

### Aligning views

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Article

# Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

## Overview

As you nest stacks together, you may want specific items within those stacks
to align with each other. By default, the alignment you specify for a stack
applies only to that stack’s child views. To align child views that reside in
the nested stacks, define a custom alignment, assign it to the enclosing view,
and use the alignment guide modifier to identify specific views to align.

### Begin with the default center alignment

To illustrate aligning items across stacks, the following view shows a
horizontal stack wrapping around two nested vertical stacks that have a
different number of child views. The enclosing `HStack` doesn’t define an
alignment, so it defaults to `center`.

The image below shows the contents of a nested vertical stack aligning at the
center of the stack. The child elements within the vertical stacks, such as
the titles beneath each image, don’t align with each other.

### Define a custom alignment

To create a new vertical alignment guide, extend `VerticalAlignment` with a
new static property for your guide. Name the guide according to what it aligns
to make it easier to use. The following example uses bottom positioning as the
default value for this guide:

### Assign and apply the custom alignment

To use the alignment guide, assign it to a parent view that encloses the views
you want to align. The following example specifies `imageTitleAlignmentGuide`
as the alignment for the horizontal stack:

The two vertical stacks now align on the bottoms of the stacks, using the
default from your specification for the custom guide.

When you define an alignment on a stack, it projects through enclosed child
views. Within the nested `VStack` instances, apply
`alignmentGuide(_:computeValue:)` to the views to align, using your custom
guide for the `HStack`.

The closure from the alignment guide modifier returns `firstTextBaseline`,
which aligns the baselines of the titles with the alignment guide
`imageTitleAlignmentGuide`.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Instance Method

# alignmentGuide(_:computeValue:)

Sets the view’s horizontal alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func alignmentGuide(
        _ g: HorizontalAlignment,
        computeValue: @escaping (ViewDimensions) -> CGFloat
    ) -> some View
    

##  Parameters

`g`

    

A `HorizontalAlignment` value at which to base the offset.

`computeValue`

    

A closure that returns the offset value to apply to this view.

## Return Value

A view modified with respect to its horizontal alignment according to the
computation performed in the method’s closure.

## Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to
reposition views in relationship to one another. You can return a constant or
can use the `ViewDimensions` argument to the closure to calculate a return
value.

In the example below, the `HStack` is offset by a constant of 50 points to the
right of center:

Changing the alignment of one view may have effects on surrounding views. Here
the offset values inside a stack and its contained views is the difference of
their absolute offsets.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Instance Method

# alignmentGuide(_:computeValue:)

Sets the view’s vertical alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func alignmentGuide(
        _ g: VerticalAlignment,
        computeValue: @escaping (ViewDimensions) -> CGFloat
    ) -> some View
    

##  Parameters

`g`

    

A `VerticalAlignment` value at which to base the offset.

`computeValue`

    

A closure that returns the offset value to apply to this view.

## Return Value

A view modified with respect to its vertical alignment according to the
computation performed in the method’s closure.

## Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to
reposition views in relationship to one another. You can return a constant or
can use the `ViewDimensions` argument to the closure to calculate a return
value.

In the example below, the weather emoji are offset 20 points from the vertical
center of the `HStack`.

Changing the alignment of one view may have effects on surrounding views. Here
the offset values inside a stack and its contained views is the difference of
their absolute offsets.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# Alignment

An alignment in both axes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Alignment

## Overview

An `Alignment` contains a `HorizontalAlignment` guide and a
`VerticalAlignment` guide. Specify an alignment to direct the behavior of
certain layout containers and modifiers, like when you place views in a
`ZStack`, or layer a view in front of or behind another view using
`overlay(alignment:content:)` or `background(alignment:content:)`,
respectively. During layout, SwiftUI brings the specified guides of the
affected views together, aligning the views.

SwiftUI provides a set of built-in alignments that represent common
combinations of the built-in horizontal and vertical alignment guides. The
blue boxes in the following diagram demonstrate the alignment named by each
box’s label, relative to the background view:

The following code generates the diagram above, where each blue box appears in
an overlay that’s configured with a different alignment:

To avoid crowding, the alignment diagram shows only two of the available text
baseline alignments. The others align as their names imply. Notice that the
first text baseline alignment aligns with the top-most line of text in the
background view, while the last text baseline aligns with the bottom-most
line. For more information about text baseline alignment, see
`VerticalAlignment`.

In a left-to-right language like English, the leading and trailing alignments
appear on the left and right edges, respectively. SwiftUI reverses these in
right-to-left language environments. For more information, see
`HorizontalAlignment`.

### Custom alignment

You can create custom alignments — which you typically do to make use of
custom horizontal or vertical guides — by using the
`init(horizontal:vertical:)` initializer. For example, you can combine a
custom vertical guide called `firstThird` with the built-in horizontal
`center` guide, and use it to configure a `ZStack`:

For more information about creating custom guides, including the code that
creates the custom `firstThird` alignment in the example above, see
`AlignmentID`.

## Topics

### Getting top guides

`static let topLeading: Alignment`

A guide that marks the top and leading edges of the view.

`static let top: Alignment`

A guide that marks the top edge of the view.

`static let topTrailing: Alignment`

A guide that marks the top and trailing edges of the view.

### Getting middle guides

`static let leading: Alignment`

A guide that marks the leading edge of the view.

`static let center: Alignment`

A guide that marks the center of the view.

`static let trailing: Alignment`

A guide that marks the trailing edge of the view.

### Getting bottom guides

`static let bottomLeading: Alignment`

A guide that marks the bottom and leading edges of the view.

`static let bottom: Alignment`

A guide that marks the bottom edge of the view.

`static let bottomTrailing: Alignment`

A guide that marks the bottom and trailing edges of the view.

### Getting text baseline guides

`static var leadingFirstTextBaseline: Alignment`

A guide that marks the leading edge and top-most text baseline in a view.

`static var centerFirstTextBaseline: Alignment`

A guide that marks the top-most text baseline in a view.

`static var trailingFirstTextBaseline: Alignment`

A guide that marks the trailing edge and top-most text baseline in a view.

`static var leadingLastTextBaseline: Alignment`

A guide that marks the leading edge and bottom-most text baseline in a view.

`static var centerLastTextBaseline: Alignment`

A guide that marks the bottom-most text baseline in a view.

`static var trailingLastTextBaseline: Alignment`

A guide that marks the trailing edge and bottom-most text baseline in a view.

### Creating a custom alignment

`init(horizontal: HorizontalAlignment, vertical: VerticalAlignment)`

Creates a custom alignment value with the specified horizontal and vertical
alignment guides.

`var horizontal: HorizontalAlignment`

The alignment on the horizontal axis.

`var vertical: VerticalAlignment`

The alignment on the vertical axis.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# HorizontalAlignment

An alignment position along the horizontal axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct HorizontalAlignment

## Overview

Use horizontal alignment guides to tell SwiftUI how to position views relative
to one another horizontally, like when you place views vertically in an
`VStack`. The following example demonstrates common built-in horizontal
alignments:

You can generate the example above by creating a series of columns implemented
as vertical stacks, where you configure each stack with a different alignment
guide:

During layout, SwiftUI aligns the views inside each stack by bringing together
the specified guides of the affected views. SwiftUI calculates the position of
a guide for a particular view based on the characteristics of the view. For
example, the `center` guide appears at half the width of the view. You can
override the guide calculation for a particular view using the
`alignmentGuide(_:computeValue:)` view modifier.

### Layout direction

When a user configures their device to use a left-to-right language like
English, the system places the leading alignment on the left and the trailing
alignment on the right, as the example from the previous section demonstrates.
However, in a right-to-left language, the system reverses these. You can see
this by using the `environment(_:_:)` view modifier to explicitly override the
`layoutDirection` environment value for the view defined above:

This automatic layout adjustment makes it easier to localize your app, but
it’s still important to test your app for the different locales that you ship
into. For more information about the localization process, see Localization.

### Custom alignment guides

You can create a custom horizontal alignment by creating a type that conforms
to the `AlignmentID` protocol, and then using that type to initalize a new
static property on `HorizontalAlignment`:

You implement the `defaultValue(in:)` method to calculate a default value for
the custom alignment guide. The method receives a `ViewDimensions` instance
that you can use to calculate an appropriate value based on characteristics of
the view. The example above places the guide at one quarter of the width of
the view, as measured from the view’s origin.

You can then use the custom alignment guide like any built-in guide. For
example, you can use it as the `alignment` parameter to a `VStack`, or you can
change it for a specific view using the `alignmentGuide(_:computeValue:)` view
modifier. Custom alignment guides also automatically reverse in a right-to-
left environment, just like built-in guides.

### Composite alignment

Combine a `VerticalAlignment` with a `HorizontalAlignment` to create a
composite `Alignment` that indicates both vertical and horizontal positioning
in one value. For example, you could combine your custom `oneQuarter`
horizontal alignment from the previous section with a built-in `center`
vertical alignment to use in a `ZStack`:

The example above uses widths and heights that generate two mismatched sets of
four vertical stripes. The `ZStack` centers the two sets vertically and aligns
them horizontally one quarter of the way from the leading edge of each set. In
a left-to-right locale, this aligns the right edges of the left-most stripes
of each set:

## Topics

### Getting guides

`static let leading: HorizontalAlignment`

A guide that marks the leading edge of the view.

`static let center: HorizontalAlignment`

A guide that marks the horizontal center of the view.

`static let trailing: HorizontalAlignment`

A guide that marks the trailing edge of the view.

`static let listRowSeparatorLeading: HorizontalAlignment`

A guide marking the leading edge of a `List` row separator.

`static let listRowSeparatorTrailing: HorizontalAlignment`

A guide marking the trailing edge of a `List` row separator.

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom horizontal alignment of the specified type.

`func combineExplicit<S>(S) -> CGFloat?`

Merges a sequence of explicit alignment values produced by this instance.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# VerticalAlignment

An alignment position along the vertical axis.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct VerticalAlignment

## Overview

Use vertical alignment guides to position views relative to one another
vertically, like when you place views side-by-side in an `HStack` or when you
create a row of views in a `Grid` using `GridRow`. The following example
demonstrates common built-in vertical alignments:

You can generate the example above by creating a series of rows implemented as
horizontal stacks, where you configure each stack with a different alignment
guide:

During layout, SwiftUI aligns the views inside each stack by bringing together
the specified guides of the affected views. SwiftUI calculates the position of
a guide for a particular view based on the characteristics of the view. For
example, the `center` guide appears at half the height of the view. You can
override the guide calculation for a particular view using the
`alignmentGuide(_:computeValue:)` view modifier.

### Text baseline alignment

Use the `firstTextBaseline` or `lastTextBaseline` guide to match the bottom of
either the top- or bottom-most line of text that a view contains,
respectively. Text baseline alignment excludes the parts of characters that
descend below the baseline, like the tail on lower case g and j:

If you use a text baseline alignment on a view that contains no text, SwiftUI
applies the equivalent of `bottom` alignment instead. For the row in the
example above, SwiftUI matches the bottom of the horizontal lines with the
baseline of the text:

Aligning a text view to its baseline rather than to the bottom of its frame
produces the best layout effect in many cases, like when creating forms. For
example, you can align the baseline of descriptive text in one `GridRow` cell
with the baseline of a text field, or the label of a checkbox, in another cell
in the same row.

### Custom alignment guides

You can create a custom vertical alignment guide by first creating a type that
conforms to the `AlignmentID` protocol, and then using that type to initalize
a new static property on `VerticalAlignment`:

You implement the `defaultValue(in:)` method to calculate a default value for
the custom alignment guide. The method receives a `ViewDimensions` instance
that you can use to calculate a value based on characteristics of the view.
The example above places the guide at one-third of the height of the view as
measured from the view’s origin.

You can then use the custom alignment guide like any built-in guide. For
example, you can use it as the `alignment` parameter to an `HStack`, or to
alter the guide calculation for a specific view using the
`alignmentGuide(_:computeValue:)` view modifier.

### Composite alignment

Combine a `VerticalAlignment` with a `HorizontalAlignment` to create a
composite `Alignment` that indicates both vertical and horizontal positioning
in one value. For example, you could combine your custom `firstThird` vertical
alignment from the previous section with a built-in `center` horizontal
alignment to use in a `ZStack`:

The example above uses widths and heights that generate two mismatched sets of
three vertical stripes. The `ZStack` centers the two sets horizontally and
aligns them vertically one-third from the top of each set. This aligns the
bottom edges of the top stripe from each set:

## Topics

### Getting guides

`static let top: VerticalAlignment`

A guide that marks the top edge of the view.

`static let center: VerticalAlignment`

A guide that marks the vertical center of the view.

`static let bottom: VerticalAlignment`

A guide that marks the bottom edge of the view.

`static let firstTextBaseline: VerticalAlignment`

A guide that marks the top-most text baseline in a view.

`static let lastTextBaseline: VerticalAlignment`

A guide that marks the bottom-most text baseline in a view.

### Creating a custom alignment

`init(any AlignmentID.Type)`

Creates a custom vertical alignment of the specified type.

`func combineExplicit<S>(S) -> CGFloat?`

Merges a sequence of explicit alignment values produced by this instance.

## Relationships

### Conforms To

  * `Equatable`
  * `Sendable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# DepthAlignment

An alignment position along the depth axis.

visionOS 1.0+

    
    
    @frozen
    struct DepthAlignment

## Topics

### Getting guides

`static let back: DepthAlignment`

A guide marking the bottom edge of the view.

`static let center: DepthAlignment`

A guide marking the vertical center of the view.

`static let front: DepthAlignment`

A guide marking the top edge of the view.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Protocol

# AlignmentID

A type that you use to create custom alignment guides.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol AlignmentID

## Overview

Every built-in alignment guide that `VerticalAlignment` or
`HorizontalAlignment` defines as a static property, like `top` or `leading`,
has a unique alignment identifier type that produces the default offset for
that guide. To create a custom alignment guide, define your own alignment
identifier as a type that conforms to the `AlignmentID` protocol, and
implement the required `defaultValue(in:)` method:

When implementing the method, calculate the guide’s default offset from the
view’s origin. If it’s helpful, you can use information from the
`ViewDimensions` input in the calculation. This parameter provides context
about the specific view that’s using the guide. The above example creates an
identifier called `FirstThirdAlignment` and calculates a default value that’s
one-third of the height of the aligned view.

Use the identifier’s type to create a static property in an extension of one
of the alignment guide types, like `VerticalAlignment`:

You can apply your custom guide like any of the built-in guides. For example,
you can use an `HStack` to align its views at one-third of their height using
the guide defined above:

Because each set of stripes has three equal, vertically stacked rectangles,
they align at the bottom edge of the top rectangle. This corresponds in each
case to a third of the overall height, as measured from the origin at the top
of each set of stripes:

You can also use the `alignmentGuide(_:computeValue:)` view modifier to alter
the behavior of your custom guide for a view, as you might alter a built-in
guide. For example, you can change one of the stacks of stripes from the
previous example to align its `firstThird` guide at two thirds of the height
instead:

The modified guide calculation causes the affected view to place the bottom
edge of its middle rectangle on the `firstThird` guide, which aligns with the
bottom edge of the top rectangle in the other two groups:

## Topics

### Getting the default value

`static func defaultValue(in: ViewDimensions) -> CGFloat`

Calculates a default value for the corresponding guide in the specified
context.

**Required**

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Structure

# ViewDimensions

A view’s size and alignment guides in its own coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ViewDimensions

## Overview

This structure contains the size and alignment guides of a view. You receive
an instance of this structure to use in a variety of layout calculations, like
when you:

  * Define a default value for a custom alignment guide; see `defaultValue(in:)`.

  * Modify an alignment guide on a view; see `alignmentGuide(_:computeValue:)`.

  * Ask for the dimensions of a subview of a custom view layout; see `dimensions(in:)`.

### Custom alignment guides

You receive an instance of this structure as the `context` parameter to the
`defaultValue(in:)` method that you implement to produce the default offset
for an alignment guide, or as the first argument to the closure you provide to
the `alignmentGuide(_:computeValue:)` view modifier to override the default
calculation for an alignment guide. In both cases you can use the instance, if
helpful, to calculate the offset for the guide. For example, you could compute
a default offset for a custom `VerticalAlignment` as a fraction of the view’s
`height`:

As another example, you could use the view dimensions instance to look up the
offset of an existing guide and modify it:

The example above indents the second text view because the subtraction moves
the second text view’s leading guide in the negative x direction, which is to
the left in the view’s coordinate space. As a result, SwiftUI moves the second
text view to the right, relative to the first text view, to keep their leading
guides aligned:

### Layout direction

The discussion above describes a left-to-right language environment, but you
don’t change your guide calculation to operate in a right-to-left environment.
SwiftUI moves the view’s origin from the left to the right side of the view
and inverts the positive x direction. As a result, the existing calculation
produces the same effect, but in the opposite direction.

You can see this if you use the `environment(_:_:)` modifier to set the
`layoutDirection` property for the view that you defined above:

With no change in your guide, this produces the desired effect — it indents
the second text view’s right side, relative to the first text view’s right
side. The leading edge is now on the right, and the direction of the offset is
reversed:

## Topics

### Getting dimensions

`var height: CGFloat`

The view’s height.

`var width: CGFloat`

The view’s width.

### Accessing guide values

`subscript(VerticalAlignment) -> CGFloat`

Gets the value of the given vertical guide.

`subscript(HorizontalAlignment) -> CGFloat`

Gets the value of the given horizontal guide.

`subscript(explicit _: VerticalAlignment) -> CGFloat?`

Gets the explicit value of the given vertical alignment guide

`subscript(explicit _: HorizontalAlignment) -> CGFloat?`

Gets the explicit value of the given horizontal alignment guide.

## Relationships

### Conforms To

  * `Equatable`

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

Instance Method

# contentMargins(_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ length: CGFloat,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`length`

    

The amount of margins to add on all edges.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# contentMargins(_:_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ edges: Edge.Set = .all,
        _ length: CGFloat?,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`edges`

    

The edges to add the margins to.

`length`

    

The amount of margins to add.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# contentMargins(_:_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ edges: Edge.Set = .all,
        _ insets: EdgeInsets,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`edges`

    

The edges to add the margins to.

`insets`

    

The amount of margins to add.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Structure

# ContentMarginPlacement

The placement of margins.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContentMarginPlacement

## Overview

Different views can support customizating margins that appear in different
parts of that view. Use values of this type to customize those margins of a
particular placement.

For example, use a `scrollIndicators` placement to customize the margins of
scrollable view’s scroll indicators separately from the margins of a
scrollable view’s content.

Use this type with the `contentMargins(_:for:)` modifier.

## Topics

### Getting the placement

`static var automatic: ContentMarginPlacement`

The automatic placement.

`static var scrollContent: ContentMarginPlacement`

The scroll content placement.

`static var scrollIndicators: ContentMarginPlacement`

The scroll indicators placement.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

Instance Method

# ignoresSafeArea(_:edges:)

Expands the safe area of a view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func ignoresSafeArea(
        _ regions: SafeAreaRegions = .all,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`regions`

    

The regions to expand the view’s safe area into. The modifier expands into all
safe area region types by default.

`edges`

    

The set of edges to expand. Any edges that you don’t include in this set
remain unchanged. The set includes all edges by default.

## Return Value

A view with an expanded safe area.

## Discussion

By default, the SwiftUI layout system sizes and positions views to avoid
certain safe areas. This ensures that system content like the software
keyboard or edges of the device don’t obstruct your views. To extend your
content into these regions, you can ignore safe areas on specific edges by
applying this modifier.

For examples of how to use this modifier, see Adding a background to your
view.

## See Also

### Staying in the safe areas

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaInset(edge:alignment:spacing:content:)

Shows the specified content beside the modified view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func safeAreaInset<V>(
        edge: HorizontalEdge,
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`edge`

    

The horizontal edge of the view to inset by the width of `content`, to make
space for `content`.

`spacing`

    

Extra distance placed between the two views, or nil to use the default amount
of spacing.

`alignment`

    

The alignment guide used to position `content` vertically.

`content`

    

A view builder function providing the view to display in the inset space of
the modified view.

## Return Value

A new view that displays `content` beside the modified view, making space for
the `content` view by horizontally insetting the modified view.

## Discussion

The `content` view is anchored to the specified horizontal edge in the parent
view, aligning its vertical axis to the specified alignment guide. The
modified view is inset by the width of `content`, from `edge`, with its safe
area increased by the same amount.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaInset(edge:alignment:spacing:content:)

Shows the specified content above or below the modified view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func safeAreaInset<V>(
        edge: VerticalEdge,
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`edge`

    

The vertical edge of the view to inset by the height of `content`, to make
space for `content`.

`spacing`

    

Extra distance placed between the two views, or nil to use the default amount
of spacing.

`alignment`

    

The alignment guide used to position `content` horizontally.

`content`

    

A view builder function providing the view to display in the inset space of
the modified view.

## Return Value

A new view that displays both `content` above or below the modified view,
making space for the `content` view by vertically insetting the modified view,
adjusting the safe area of the result to match.

## Discussion

The `content` view is anchored to the specified vertical edge in the parent
view, aligning its horizontal axis to the specified alignment guide. The
modified view is inset by the height of `content`, from `edge`, with its safe
area increased by the same amount.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(_ insets: EdgeInsets) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(_ length: CGFloat) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(
        _ edges: Edge.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Structure

# SafeAreaRegions

A set of symbolic safe area regions.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @frozen
    struct SafeAreaRegions

## Topics

### Getting safe area regions

`static let all: SafeAreaRegions`

All safe area regions.

`static let container: SafeAreaRegions`

The safe area defined by the device and containers within the user interface,
including elements such as top and bottom bars.

`static let keyboard: SafeAreaRegions`

The safe area matching the current extent of any software keyboard displayed
over the view content.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

Instance Method

# layoutDirectionBehavior(_:)

Sets the behavior of this view for different layout directions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func layoutDirectionBehavior(_ behavior: LayoutDirectionBehavior) -> some View
    

##  Parameters

`behavior`

    

A LayoutDirectionBehavior value that indicates whether this view should mirror
in a particular layout direction. By default, views will adjust their layouts
automatically in a right-to-left context and do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally in a given layout
direction.

## Discussion

Use `layoutDirectionBehavior(_:)` when you need the system to horizontally
mirror the contents of the view when presented in a layout direction.

To override the layout direction for a specific view, use the
`environment(_:_:)` view modifier to explicitly override the `layoutDirection`
environment value for the view.

## See Also

### Setting a layout direction

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Enumeration

# LayoutDirectionBehavior

A description of what should happen when the layout direction changes.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    enum LayoutDirectionBehavior

## Overview

A `LayoutDirectionBehavior` can be used with the `layoutDirectionBehavior`
view modifier or the `layoutDirectionBehavior` property of `Shape`.

## Topics

### Getting behaviors

`case fixed`

A behavior that doesn’t mirror when the layout direction changes.

`static var mirrors: LayoutDirectionBehavior`

A behavior that mirrors when the layout direction is right-to-left.

`case mirrors(in: LayoutDirection)`

A behavior that mirrors when the layout direction has the specified value.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Instance Property

# layoutDirection

The layout direction associated with the current environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var layoutDirection: LayoutDirection { get set }

## Discussion

Use this value to determine or set whether the environment uses a left-to-
right or right-to-left direction.

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Enumeration

# LayoutDirection

A direction in which SwiftUI can lay out content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum LayoutDirection

## Overview

SwiftUI supports both left-to-right and right-to-left directions for laying
out content to support different languages and locales. The system sets the
value based on the user’s locale, but you can also use the `environment(_:_:)`
modifier to override the direction for a view and its child views:

You can also read the `layoutDirection` environment value to find out which
direction applies to a particular environment. However, in many cases, you
don’t need to take any action based on this value. SwiftUI horizontally flips
the x position of each view within its parent, so layout calculations
automatically produce the desired effect for both modes without any changes.

## Topics

### Getting layout directions

`case leftToRight`

A left-to-right layout direction.

`case rightToLeft`

A right-to-left layout direction.

### Creating a layout direction

`init?(UITraitEnvironmentLayoutDirection)`

Create a direction from its UITraitEnvironmentLayoutDirection equivalent.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Setting a layout direction

`func layoutDirectionBehavior(LayoutDirectionBehavior) -> some View`

Sets the behavior of this view for different layout directions.

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

Instance Property

# isLuminanceReduced

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var isLuminanceReduced: Bool { get set }

## Discussion

When you detect this condition, lower the overall brightness of your view. For
example, you can change large, filled shapes to be stroked, and choose less
bright colors:

In addition to the changes that you make, the system could also dim the
display to achieve a suitable brightness. By reacting to `isLuminanceReduced`,
you can preserve contrast and readability while helping to satisfy the reduced
brightness requirement.

Note

On watchOS, the system typically sets this value to `true` when the user
lowers their wrist, but the display remains on. Starting in watchOS 8, the
system keeps your view visible on wrist down by default. If you want the
system to blur the screen instead, as it did in earlier versions of watchOS,
set the value for the `WKSupportsAlwaysOnDisplay` key in your app’s
Information Property List file to `false`.

## See Also

### Reacting to interface characteristics

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# displayScale

The display scale of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var displayScale: CGFloat { get set }

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# pixelLength

The size of a pixel on the screen.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var pixelLength: CGFloat { get }

## Discussion

This value is usually equal to `1` divided by `displayScale`.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# horizontalSizeClass

The horizontal size class of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
    var horizontalSizeClass: UserInterfaceSizeClass? { get set }

## Discussion

You receive a `UserInterfaceSizeClass` value when you read this environment
value. The value tells you about the amount of horizontal space available to
the view that reads it. You can read this size class like any other of the
`EnvironmentValues`, by creating a property with the `Environment` property
wrapper:

SwiftUI sets this size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

  * The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on this size class. For
example, a `NavigationView` presents a multicolumn view when the horizontal
size class is `UserInterfaceSizeClass.regular`, but a single column otherwise.
You can also adjust the appearance of custom views by reading the size class
and conditioning your views. If you do, be prepared to handle size class
changes while your app runs, because factors like device orientation can
change at runtime.

In watchOS, the horizontal size class is always
`UserInterfaceSizeClass.compact`. In macOS, and tvOS, it’s always
`UserInterfaceSizeClass.regular`.

Writing to the horizontal size class in the environment before macOS 14.0,
tvOS 17.0, and watchOS 10.0 is not supported.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Instance Property

# verticalSizeClass

The vertical size class of this environment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
    var verticalSizeClass: UserInterfaceSizeClass? { get set }

## Discussion

You receive a `UserInterfaceSizeClass` value when you read this environment
value. The value tells you about the amount of vertical space available to the
view that reads it. You can read this size class like any other of the
`EnvironmentValues`, by creating a property with the `Environment` property
wrapper:

SwiftUI sets this size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

You can adjust the appearance of custom views by reading this size class and
conditioning your views. If you do, be prepared to handle size class changes
while your app runs, because factors like device orientation can change at
runtime.

In watchOS, the vertical size class is always
`UserInterfaceSizeClass.compact`. In macOS, and tvOS, it’s always
`UserInterfaceSizeClass.regular`.

Writing to the vertical size class in the environment before macOS 14.0, tvOS
17.0, and watchOS 10.0 is not supported.

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`enum UserInterfaceSizeClass`

A set of values that indicate the visual size available to the view.

Enumeration

# UserInterfaceSizeClass

A set of values that indicate the visual size available to the view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    enum UserInterfaceSizeClass

## Overview

You receive a size class value when you read either the `horizontalSizeClass`
or `verticalSizeClass` environment value. The value tells you about the amount
of space available to your views in a given direction. You can read the size
class like any other of the `EnvironmentValues`, by creating a property with
the `Environment` property wrapper:

SwiftUI sets the size class based on several factors, including:

  * The current device type.

  * The orientation of the device.

  * The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on the size class. For
example, a `NavigationView` presents a multicolumn view when the horizontal
size class is `UserInterfaceSizeClass.regular`, but a single column otherwise.
You can also adjust the appearance of custom views by reading the size class
and conditioning your views. If you do, be prepared to handle size class
changes while your app runs, because factors like device orientation can
change at runtime.

## Topics

### Getting size classes

`case compact`

The compact size class.

`case regular`

The regular size class.

### Creating a size class

`init?(UIUserInterfaceSizeClass)`

Creates a SwiftUI size class from the specified UIKit size class.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Reacting to interface characteristics

`var isLuminanceReduced: Bool`

A Boolean value that indicates whether the display or environment currently
requires reduced luminance.

`var displayScale: CGFloat`

The display scale of this environment.

`var pixelLength: CGFloat`

The size of a pixel on the screen.

`var horizontalSizeClass: UserInterfaceSizeClass?`

The horizontal size class of this environment.

`var verticalSizeClass: UserInterfaceSizeClass?`

The vertical size class of this environment.

Enumeration

# Edge

An enumeration to indicate one edge of a rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    enum Edge

## Topics

### Getting the edges

`case top`

`case bottom`

`case leading`

`case trailing`

### Creating an edge

`init?(Edge3D)`

Converts a 3D edge to a 2D edge, if possible.

### Accessing sets of edges

`struct Set`

An efficient set of edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Enumeration

# Edge3D

An edge or face of a 3D volume.

visionOS 1.0+

    
    
    @frozen
    enum Edge3D

## Topics

### Getting the edges

`case top`

`case bottom`

`case leading`

`case trailing`

`case front`

`case back`

### Creating an edge

`init(Edge)`

### Accessing sets of edges

`struct Set`

An efficient set of 3D edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Enumeration

# HorizontalEdge

An edge on the horizontal axis.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum HorizontalEdge

## Overview

Use a horizontal edge for tasks like setting a swipe action with the
`swipeActions(edge:allowsFullSwipe:content:)` view modifier. The positions of
the leading and trailing edges depend on the locale chosen by the user.

## Topics

### Getting the edges

`case leading`

The leading edge.

`case trailing`

The trailing edge.

### Accessing sets of edges

`struct Set`

An efficient set of horizontal edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Enumeration

# VerticalEdge

An edge on the vertical axis.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @frozen
    enum VerticalEdge

## Topics

### Getting the edges

`case top`

The top edge.

`case bottom`

The bottom edge.

### Accessing sets of edges

`struct Set`

An efficient set of vertical edges.

## Relationships

### Conforms To

  * `CaseIterable`
  * `Decodable`
  * `Encodable`
  * `Equatable`
  * `Hashable`
  * `RawRepresentable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Structure

# EdgeInsets

The inset distances for the sides of a rectangle.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct EdgeInsets

## Topics

### Getting edge insets

`var top: CGFloat`

`var bottom: CGFloat`

`var leading: CGFloat`

`var trailing: CGFloat`

### Creating an edge inset

`init()`

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)`

`init(EdgeInsets3D)`

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and
`back` values.

`init(NSDirectionalEdgeInsets)`

Create edge insets from the equivalent NSDirectionalEdgeInsets.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets3D`

The inset distances for the faces of a 3D volume.

Structure

# EdgeInsets3D

The inset distances for the faces of a 3D volume.

visionOS 1.0+

    
    
    @frozen
    struct EdgeInsets3D

## Topics

### Getting edge insets

`var top: CGFloat`

The inset distance along the top face of a 3D volume.

`var bottom: CGFloat`

The inset distance along the bottom face of a 3D volume.

`var leading: CGFloat`

The inset distance along the leading face of a 3D volume.

`var trailing: CGFloat`

The inset distance along the top trailing of a 3D volume.

`var front: CGFloat`

The inset distance along the top front of a 3D volume.

`var back: CGFloat`

The inset distance along the top back of a 3D volume.

### Creating an edge inset

`init(horizontal: CGFloat, vertical: CGFloat, depth: CGFloat)`

Creates an `EdgeInsets3D` value with values provided for each axis.

`init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat,
front: CGFloat, back: CGFloat)`

Creates an `EdgeInsets3D` value with values provided for each face.

## Relationships

### Conforms To

  * `Animatable`
  * `Equatable`
  * `Sendable`

## See Also

### Accessing edges and regions

`enum Edge`

An enumeration to indicate one edge of a rectangle.

`enum Edge3D`

An edge or face of a 3D volume.

`enum HorizontalEdge`

An edge on the horizontal axis.

`enum VerticalEdge`

An edge on the vertical axis.

`struct EdgeInsets`

The inset distances for the sides of a rectangle.



# Layout modifiers

Instance Method

# frame(width:height:alignment:)

Positions this view within an invisible frame with the specified size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame(
        width: CGFloat? = nil,
        height: CGFloat? = nil,
        alignment: Alignment = .center
    ) -> some View
    

##  Parameters

`width`

    

A fixed width for the resulting view. If `width` is `nil`, the resulting view
assumes this view’s sizing behavior.

`height`

    

A fixed height for the resulting view. If `height` is `nil`, the resulting
view assumes this view’s sizing behavior.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with fixed dimensions of `width` and `height`, for the parameters that
are non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s width, height, or both.
If you only specify one of the dimensions, the resulting view assumes this
view’s sizing behavior in the other dimension.

For example, the following code lays out an ellipse in a fixed 200 by 100
frame. Because a shape always occupies the space offered to it by the layout
system, the first ellipse is 200x100 points. The second ellipse is laid out in
a frame with only a fixed height, so it occupies that height, and whatever
width the layout system offers to its parent.

`The alignment` parameter specifies this view’s alignment within the frame.

In the example above, the text is positioned at the top, leading corner of the
frame. If the text is taller than the frame, its bounds may extend beyond the
bottom of the frame’s bounds.

## See Also

### Influencing a view’s size

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# frame(depth:alignment:)

Positions this view within an invisible frame with the specified depth.

visionOS 1.0+

    
    
    func frame(
        depth: CGFloat?,
        alignment: DepthAlignment = .center
    ) -> some View
    

##  Parameters

`depth`

    

A fixed depth for the resulting view. If `depth` is `nil`, the resulting view
assumes this view’s sizing behavior.

`alignment`

    

The alignment of this view inside the resulting view. `alignment` applies if
this view is smaller than the size given by the resulting frame.

## Return Value

A view with a fixed dimension of `depth` if non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s depth. If you don’t
specify a dimension, the resulting view assumes this view’s sizing behavior in
depth.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

#
frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)

Positions this view within an invisible frame having the specified size
constraints.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func frame(
        minWidth: CGFloat? = nil,
        idealWidth: CGFloat? = nil,
        maxWidth: CGFloat? = nil,
        minHeight: CGFloat? = nil,
        idealHeight: CGFloat? = nil,
        maxHeight: CGFloat? = nil,
        alignment: Alignment = .center
    ) -> some View
    

##  Parameters

`minWidth`

    

The minimum width of the resulting frame.

`idealWidth`

    

The ideal width of the resulting frame.

`maxWidth`

    

The maximum width of the resulting frame.

`minHeight`

    

The minimum height of the resulting frame.

`idealHeight`

    

The ideal height of the resulting frame.

`maxHeight`

    

The maximum height of the resulting frame.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass
`nil` or leave out a characteristic to indicate that the frame should adopt
this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by
any constraints specified, and with any ideal dimensions specified replacing
any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the
frame adopts the sizing behavior of its child in that dimension. If both
constraints are specified in a dimension, the frame unconditionally adopts the
size proposed for it, clamped to the constraints. Otherwise, the size of the
frame in either dimension is:

  * If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.

  * If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.

  * Otherwise, the size of this view.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# frame(minDepth:idealDepth:maxDepth:alignment:)

Positions this view within an invisible frame having the specified depth
constraints.

visionOS 1.0+

    
    
    func frame(
        minDepth: CGFloat? = nil,
        idealDepth: CGFloat? = nil,
        maxDepth: CGFloat? = nil,
        alignment: DepthAlignment = .center
    ) -> some View
    

##  Parameters

`minDepth`

    

The minimum depth of the resulting frame.

`idealDepth`

    

The ideal depth of the resulting frame.

`maxDepth`

    

The maximum depth of the resulting frame.

`alignment`

    

The alignment of this view inside the resulting frame. Note that most
alignment values have no apparent effect when the size of the frame happens to
match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass
`nil` or leave out a characteristic to indicate that the frame should adopt
this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by
any constraints specified, and with an ideal dimension specified replacing any
corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the
frame adopts the sizing behavior of its child in that dimension. If both
constraints are specified in a dimension, the frame unconditionally adopts the
size proposed for it, clamped to the constraints. Otherwise, the size of the
frame in either dimension is:

  * If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.

  * If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.

  * Otherwise, the size of this view.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:alignment:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        alignment: Alignment = .center
    ) -> some View
    

## Discussion

Use this modifier to specify a size for a view’s width, height, or both that
is dependent on the size of the nearest container. Different things can
represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use the `containerRelativeFrame(_:count:span:spacing:alignment:)` modifier to
size a view such that multiple views will be visible in the container. When
using this modifier, the count refers to the total number of rows or columns
that the length of the container size in a particular axis should be divided
into. The span refers to the number of rows or columns that the modified view
should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use the `containerRelativeFrame(_:alignment:_:)` modifier to apply your own
custom logic to adjust the size of the nearest container for your view. The
following example will result in the container frame’s width being divided by
3 and using that value as the width of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:alignment:_:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        alignment: Alignment = .center,
        _ length: @escaping (CGFloat, Axis) -> CGFloat
    ) -> some View
    

## Discussion

Use the `containerRelativeFrame(_:alignment:)` modifier to specify a size for
a view’s width, height, or both that is dependent on the size of the nearest
container. Different things can represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use the `View/containerRelativeFrame(_:count:spacing:alignment:)` modifier to
size a view such that multiple views will be visible in the container. When
using this modifier, the count refers to the total number of rows or columns
that the length of the container size in a particular axis should be divided
into. The span refers to the number of rows or columns that the modified view
should actually occupy. Thus the size of the element can be described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use this modifier to apply your own custom logic to adjust the size of the
nearest container for your view. The following example will result in the
container frame’s width being divided by 3 and using that value as the width
of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# containerRelativeFrame(_:count:span:spacing:alignment:)

Positions this view within an invisible frame with a size relative to the
nearest container.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerRelativeFrame(
        _ axes: Axis.Set,
        count: Int,
        span: Int = 1,
        spacing: CGFloat,
        alignment: Alignment = .center
    ) -> some View
    

## Discussion

Use the `containerRelativeFrame(_:alignment:)` modifier to specify a size for
a view’s width, height, or both that is dependent on the size of the nearest
container. Different things can represent a “container” including:

  * The window presenting a view on iPadOS or macOS, or the screen of a device on iOS.

  * A column of a NavigationSplitView

  * A NavigationStack

  * A tab of a TabView

  * A scrollable view like ScrollView or List

The size provided to this modifier is the size of a container like the ones
listed above subtracting any safe area insets that might be applied to that
container.

The following example will have each purple rectangle occupy the full size of
the screen on iOS:

Use this modifier to size a view such that multiple views will be visible in
the container. When using this modifier, the count refers to the total number
of rows or columns that the length of the container size in a particular axis
should be divided into. The span refers to the number of rows or columns that
the modified view should actually occupy. Thus the size of the element can be
described like so:

The following example only uses the nearest container size in the horizontal
axis, allowing the vertical axis to be determined using the
`aspectRatio(_:contentMode:)` modifier.

Use the `containerRelativeFrame(_:alignment:_:)` modifier to apply your own
custom logic to adjust the size of the nearest container for your view. The
following example will result in the container frame’s width being divided by
3 and using that value as the width of the purple rectangle.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# fixedSize()

Fixes this view at its ideal size.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fixedSize() -> some View
    

## Return Value

A view that fixes this view at its ideal size.

## Discussion

During the layout of the view hierarchy, each view proposes a size to each
child view it contains. If the child view doesn’t need a fixed size it can
accept and conform to the size offered by the parent.

For example, a `Text` view placed in an explicitly sized frame wraps and
truncates its string to remain within its parent’s bounds:

The `fixedSize()` modifier can be used to create a view that maintains the
_ideal size_ of its children both dimensions:

This can result in the view exceeding the parent’s bounds, which may or may
not be the effect you want.

You can think of `fixedSize()` as the creation of a _counter proposal_ to the
view size proposed to a view by its parent. The ideal size of a view, and the
specific effects of `fixedSize()` depends on the particular view and how you
have configured it.

To create a view that fixes the view’s size in either the horizontal or
vertical dimensions, see `fixedSize(horizontal:vertical:)`.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# fixedSize(horizontal:vertical:)

Fixes this view at its ideal size in the specified dimensions.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func fixedSize(
        horizontal: Bool,
        vertical: Bool
    ) -> some View
    

##  Parameters

`horizontal`

    

A Boolean value that indicates whether to fix the width of the view.

`vertical`

    

A Boolean value that indicates whether to fix the height of the view.

## Return Value

A view that fixes this view at its ideal size in the dimensions specified by
`horizontal` and `vertical`.

## Discussion

This function behaves like `fixedSize()`, except with
`fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally
specified in one or both dimensions. For example, if you horizontally fix a
text view before wrapping it in the frame view, you’re telling the text view
to maintain its ideal _width_. The view calculates this to be the space needed
to represent the entire string.

This can result in the view exceeding the parent’s bounds, which may or may
not be the effect you want.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func layoutPriority(Double) -> some View`

Sets the priority by which a parent layout should apportion space to this
child.

Instance Method

# layoutPriority(_:)

Sets the priority by which a parent layout should apportion space to this
child.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func layoutPriority(_ value: Double) -> some View
    

##  Parameters

`value`

    

The priority by which a parent layout apportions space to the child.

## Discussion

Views typically have a default priority of `0` which causes space to be
apportioned evenly to all sibling views. Raising a view’s layout priority
encourages the higher priority view to shrink later when the group is shrunk
and stretch sooner when the group is stretched.

In the example above, the first `Text` element has the default priority `0`
which causes its view to shrink dramatically due to the higher priority of the
second `Text` element, even though all of their other attributes (font, font
size and character count) are the same.

A parent layout offers the child views with the highest layout priority all
the space offered to the parent minus the minimum space required for all its
lower-priority children.

## See Also

### Influencing a view’s size

`func frame(width: CGFloat?, height: CGFloat?, alignment: Alignment) -> some
View`

Positions this view within an invisible frame with the specified size.

`func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame with the specified depth.

`func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?,
minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment:
Alignment) -> some View`

Positions this view within an invisible frame having the specified size
constraints.

`func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?,
alignment: DepthAlignment) -> some View`

Positions this view within an invisible frame having the specified depth
constraints.

`func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis)
-> CGFloat) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing:
CGFloat, alignment: Alignment) -> some View`

Positions this view within an invisible frame with a size relative to the
nearest container.

`func fixedSize() -> some View`

Fixes this view at its ideal size.

`func fixedSize(horizontal: Bool, vertical: Bool) -> some View`

Fixes this view at its ideal size in the specified dimensions.

Instance Method

# position(_:)

Positions the center of this view at the specified point in its parent’s
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func position(_ position: CGPoint) -> some View
    

##  Parameters

`position`

    

The point at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `position`.

## Discussion

Use the `position(_:)` modifier to place the center of a view at a specific
coordinate in the parent view using a `CGPoint` to specify the `x` and `y`
offset.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# position(x:y:)

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func position(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`x`

    

The x-coordinate at which to place the center of this view.

`y`

    

The y-coordinate at which to place the center of this view.

## Return Value

A view that fixes the center of this view at `x` and `y`.

## Discussion

Use the `position(x:y:)` modifier to place the center of a view at a specific
coordinate in the parent view using an `x` and `y` offset.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(_:)

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(_ offset: CGSize) -> some View
    

##  Parameters

`offset`

    

The distance to offset this view.

## Return Value

A view that offsets this view by `offset`.

## Discussion

Use `offset(_:)` to shift the displayed contents by the amount specified in
the `offset` parameter.

The original dimensions of the view aren’t changed by offsetting the contents;
in the example below the gray border drawn by this view surrounds the original
position of the text:

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(x:y:)

Offset this view by the specified horizontal and vertical distances.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func offset(
        x: CGFloat = 0,
        y: CGFloat = 0
    ) -> some View
    

##  Parameters

`x`

    

The horizontal distance to offset this view.

`y`

    

The vertical distance to offset this view.

## Return Value

A view that offsets this view by `x` and `y`.

## Discussion

Use `offset(x:y:)` to shift the displayed contents by the amount specified in
the `x` and `y` parameters.

The original dimensions of the view aren’t changed by offsetting the contents;
in the example below the gray border drawn by this view surrounds the original
position of the text:

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(z: CGFloat) -> some View`

Brings a view forward in Z by the provided distance in points.

Instance Method

# offset(z:)

Brings a view forward in Z by the provided distance in points.

visionOS 1.0+

    
    
    func offset(z: CGFloat) -> some View
    

##  Parameters

`distance`

    

The distance to extrude the view forward in Z, in points.

## Return Value

A view that is extruded forward in Z by `distance`.

## See Also

### Adjusting a view’s position

Making fine adjustments to a view’s position

Shift the position of a view by applying the offset or position modifier.

`func position(CGPoint) -> some View`

Positions the center of this view at the specified point in its parent’s
coordinate space.

`func position(x: CGFloat, y: CGFloat) -> some View`

Positions the center of this view at the specified coordinates in its parent’s
coordinate space.

`func offset(CGSize) -> some View`

Offset this view by the horizontal and vertical amount specified in the offset
parameter.

`func offset(x: CGFloat, y: CGFloat) -> some View`

Offset this view by the specified horizontal and vertical distances.

Instance Method

# coordinateSpace(_:)

Assigns a name to the view’s coordinate space, so other code can operate on
dimensions like points and sizes relative to the named space.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func coordinateSpace(_ name: NamedCoordinateSpace) -> some View
    

##  Parameters

`name`

    

A name used to identify this coordinate space.

## Discussion

Use `coordinateSpace(_:)` to allow another function to find and operate on a
view and operate on dimensions relative to that view.

The example below demonstrates how a nested view can find and operate on its
enclosing view’s coordinate space:

Here, the `VStack` in the `ContentView` named “stack” is composed of a red
frame with a custom `Circle` view `overlay(_:alignment:)` at its center.

The `circle` view has an attached `DragGesture` that targets the enclosing
VStack’s coordinate space. As the gesture recognizer’s closure registers
events inside `circle` it stores them in the shared `location` state variable
and the `VStack` displays the coordinates in a `Text` view.

## See Also

### Measuring a view

`struct GeometryReader`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryReader3D`

A container view that defines its content as a function of its own size and
coordinate space.

`struct GeometryProxy`

A proxy for access to the size and coordinate space (for anchor resolution) of
the container view.

`struct GeometryProxy3D`

A proxy for access to the size and coordinate space of the container view.

`enum CoordinateSpace`

A resolved coordinate space created by the coordinate space protocol.

`protocol CoordinateSpaceProtocol`

A frame of reference within the layout system.

`struct PhysicalMetric`

Provides access to a value in points that corresponds to the specified
physical measurement.

`struct PhysicalMetricsConverter`

A physical metrics converter provides conversion between point values and
their extent in 3D space, in the form of physical length measurements.

Instance Method

# alignmentGuide(_:computeValue:)

Sets the view’s horizontal alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func alignmentGuide(
        _ g: HorizontalAlignment,
        computeValue: @escaping (ViewDimensions) -> CGFloat
    ) -> some View
    

##  Parameters

`g`

    

A `HorizontalAlignment` value at which to base the offset.

`computeValue`

    

A closure that returns the offset value to apply to this view.

## Return Value

A view modified with respect to its horizontal alignment according to the
computation performed in the method’s closure.

## Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to
reposition views in relationship to one another. You can return a constant or
can use the `ViewDimensions` argument to the closure to calculate a return
value.

In the example below, the `HStack` is offset by a constant of 50 points to the
right of center:

Changing the alignment of one view may have effects on surrounding views. Here
the offset values inside a stack and its contained views is the difference of
their absolute offsets.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(VerticalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s vertical alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Instance Method

# alignmentGuide(_:computeValue:)

Sets the view’s vertical alignment.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func alignmentGuide(
        _ g: VerticalAlignment,
        computeValue: @escaping (ViewDimensions) -> CGFloat
    ) -> some View
    

##  Parameters

`g`

    

A `VerticalAlignment` value at which to base the offset.

`computeValue`

    

A closure that returns the offset value to apply to this view.

## Return Value

A view modified with respect to its vertical alignment according to the
computation performed in the method’s closure.

## Discussion

Use `alignmentGuide(_:computeValue:)` to calculate specific offsets to
reposition views in relationship to one another. You can return a constant or
can use the `ViewDimensions` argument to the closure to calculate a return
value.

In the example below, the weather emoji are offset 20 points from the vertical
center of the `HStack`.

Changing the alignment of one view may have effects on surrounding views. Here
the offset values inside a stack and its contained views is the difference of
their absolute offsets.

## See Also

### Aligning views

Aligning views within a stack

Position views inside a stack using alignment guides.

Aligning views across stacks

Create a custom alignment and use it to align views across multiple stacks.

`func alignmentGuide(HorizontalAlignment, computeValue: (ViewDimensions) ->
CGFloat) -> some View`

Sets the view’s horizontal alignment.

`struct Alignment`

An alignment in both axes.

`struct HorizontalAlignment`

An alignment position along the horizontal axis.

`struct VerticalAlignment`

An alignment position along the vertical axis.

`struct DepthAlignment`

An alignment position along the depth axis.

`protocol AlignmentID`

A type that you use to create custom alignment guides.

`struct ViewDimensions`

A view’s size and alignment guides in its own coordinate space.

Instance Method

# padding(_:)

Adds a specific padding amount to each edge of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(_ length: CGFloat) -> some View
    

##  Parameters

`length`

    

The amount, given in points, to pad this view on all edges.

## Return Value

A view that’s padded by the amount you specify.

## Discussion

Use this modifier to add padding all the way around a view.

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

To independently control the amount of padding for each edge, use
`padding(_:)`. To pad a select set of edges by the same amount, use
`padding(_:_:)`.

## See Also

### Adding padding around a view

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding(_:_:)

Adds an equal padding amount to specific edges of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(
        _ edges: Edge.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

##  Parameters

`edges`

    

The set of edges to pad for this view. The default is `all`.

`length`

    

An amount, given in points, to pad this view on the specified edges. If you
set the value to `nil`, SwiftUI uses a platform-specific default amount. The
default value of this parameter is `nil`.

## Return Value

A view that’s padded by the specified amount on the specified edges.

## Discussion

Use this modifier to add a specified amount of padding to one or more edges of
the view. Indicate the edges to pad by naming either a single value from
`Edge.Set`, or by specifying an `OptionSet` that contains edge values:

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

You can omit either or both of the parameters. If you omit the `length`,
SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI
applies the padding to all edges. Omit both to add a default padding all the
way around a view. SwiftUI chooses a default amount of padding that’s
appropriate for the platform and the presentation context.

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use
`padding(_:)`. To pad all outside edges of a view by a specified amount, use
`padding(_:)`.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding(_:)

Adds a different padding amount to each edge of this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func padding(_ insets: EdgeInsets) -> some View
    

##  Parameters

`insets`

    

An `EdgeInsets` instance that contains padding amounts for each edge.

## Return Value

A view that’s padded by different amounts on each edge.

## Discussion

Use this modifier to add a different amount of padding on each edge of a view:

The order in which you apply modifiers matters. The example above applies the
padding before applying the border to ensure that the border encompasses the
padded region:

To pad a view on specific edges with equal padding for all padded edges, use
`padding(_:_:)`. To pad all edges of a view equally, use `padding(_:)`.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:)

Pads this view along all edge insets by the amount you specify.

visionOS 1.0+

    
    
    func padding3D(_ length: CGFloat) -> some View
    

##  Parameters

`length`

    

The amount to inset this view on each edge.

## Return Value

A view that pads this view by the amount you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:)

Pads this view using the edge insets you specify.

visionOS 1.0+

    
    
    func padding3D(_ insets: EdgeInsets3D) -> some View
    

##  Parameters

`insets`

    

The edges to inset.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# padding3D(_:_:)

Pads this view using the edge insets you specify.

visionOS 1.0+

    
    
    func padding3D(
        _ edges: Edge3D.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

##  Parameters

`edges`

    

The set of edges along which to inset this view.

`length`

    

The amount to inset this view on each edge. If `nil`, the amount is the system
default amount.

## Return Value

A view that pads this view using edge the insets you specify.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# listRowInsets(_:)

Applies an inset to the rows in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowInsets(_ insets: EdgeInsets?) -> some View
    

##  Parameters

`insets`

    

The `EdgeInsets` to apply to the edges of the view.

## Return Value

A view that uses the given edge insets when used as a list cell.

## Discussion

Use `listRowInsets(_:)` to change the default padding of the content of list
items.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowInsets(_:)`
modifier then changes the edge insets of each row of the list according to the
`EdgeInsets` provided:

## See Also

### Configuring rows

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# scenePadding(_:)

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func scenePadding(_ edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view.
Specify either a single edge value from `Edge.Set`, or an `OptionSet` that
describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root
view of a window. In watchOS, use scene padding to align elements of your user
interface with top level elements, like the title of a navigation view. For
example, compare the effects of different kinds of padding on text views
presented inside a `NavigationView` in watchOS:

The text with scene padding automatically aligns with the title, unlike the
text that uses the default padding or the text without padding:

Scene padding in watchOS also ensures that your content avoids the curved
edges of a device like Apple Watch Series 7. In other platforms, scene padding
produces the same default padding that you get from the `padding(_:_:)`
modifier.

Important

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even
if you specify those edges as part of the input. For example, if you specify
`vertical` instead of `horizontal` in the example above, the modifier would
have no effect in watchOS. It does, however, apply to all the edges that you
specify in other platforms.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(ScenePadding, edges: Edge.Set) -> some View`

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# scenePadding(_:edges:)

Adds a specified kind of padding to the specified edges of this view using an
amount that’s appropriate for the current scene.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func scenePadding(
        _ padding: ScenePadding,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`padding`

    

The kind of padding to add.

`edges`

    

The set of edges along which to pad this view.

## Return Value

A view that’s padded on specified edges by a scene-appropriate amount.

## Discussion

Use this modifier to add a scene-appropriate amount of padding to a view.
Specify either a single edge value from `Edge.Set`, or an `OptionSet` that
describes the edges to pad.

In macOS, use scene padding to produce the recommended spacing around the root
view of a window. In watchOS, use scene padding to align elements of your user
interface with top level elements, like the title of a navigation view. For
example, compare the effects of different kinds of padding on text views
presented inside a `NavigationView` in watchOS:

The text with minimum scene padding uses the system minimum padding and the
text with navigation bar scene padding automatically aligns with the
navigation bar content. In contrast, the text that uses the default padding
and the text without padding do not align with scene elements.

Scene padding in watchOS also ensures that your content avoids the curved
edges of a device like Apple Watch Series 7. In other platforms, scene padding
produces the same default padding that you get from the `padding(_:_:)`
modifier.

Important

Scene padding doesn’t pad the top and bottom edges of a view in watchOS, even
if you specify those edges as part of the input. For example, if you specify
`vertical` instead of `horizontal` in the example above, the modifier would
have no effect in watchOS. It does, however, apply to all the edges that you
specify in other platforms.

## See Also

### Adding padding around a view

`func padding(CGFloat) -> some View`

Adds a specific padding amount to each edge of this view.

`func padding(Edge.Set, CGFloat?) -> some View`

Adds an equal padding amount to specific edges of this view.

`func padding(EdgeInsets) -> some View`

Adds a different padding amount to each edge of this view.

`func padding3D(CGFloat) -> some View`

Pads this view along all edge insets by the amount you specify.

`func padding3D(EdgeInsets3D) -> some View`

Pads this view using the edge insets you specify.

`func padding3D(Edge3D.Set, CGFloat?) -> some View`

Pads this view using the edge insets you specify.

`func scenePadding(Edge.Set) -> some View`

Adds padding to the specified edges of this view using an amount that’s
appropriate for the current scene.

`struct ScenePadding`

The padding used to space a view from its containing scene.

Instance Method

# listRowSpacing(_:)

Sets the vertical spacing between two adjacent rows in a List.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSpacing(_ spacing: CGFloat?) -> some View
    

##  Parameters

`spacing`

    

The spacing value to use. A value of `nil` uses the default spacing.

## Discussion

The following example creates a List with 10 pts of spacing between each row:

## See Also

### Configuring spacing

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing to a custom value between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: CGFloat) -> some View
    

##  Parameters

`spacing`

    

the amount of spacing to apply.

## Discussion

The following example creates a List with 5 pts of spacing between sections:

Spacing can also be specified on a per-section basis. The following example
creates a List with compact spacing for its second section:

If adjacent sections have different spacing value, the smaller value on the
shared edge is used. Spacing specified inside the List is preferred over any
List-wide value.

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: ListSectionSpacing) -> some View
    

## Discussion

Pass `.default` for the default spacing, or use `.compact` for a compact
appearance between sections.

The following example creates a List with compact spacing between sections:

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# gridCellColumns(_:)

Tells a view that acts as a cell in a grid to span the specified number of
columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellColumns(_ count: Int) -> some View
    

##  Parameters

`count`

    

The number of columns that the view should consume when placed in a grid row.

## Return Value

A view that occupies the specified number of columns in a grid row.

## Discussion

By default, each view that you put into the content closure of a `GridRow`
corresponds to exactly one column of the grid. Apply the `gridCellColumns(_:)`
modifier to a view that you want to span more than one column, as in the
following example of a typical macOS configuration view:

The `Toggle` in the example above spans the column that contains the font
names and the column that contains the buttons:

Important

When you tell a cell to span multiple columns, the grid changes the merged
cell to use anchor alignment, rather than the usual alignment guides. For
information about the behavior of anchor alignment, see `gridCellAnchor(_:)`.

As a convenience you can cause a view to span all of the `Grid` columns by
placing the view directly in the content closure of the `Grid`, outside of a
`GridRow`, and omitting the modifier. To do the opposite and include more than
one view in a cell, group the views using an appropriate layout container,
like an `HStack`, so that they act as a single view.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellAnchor(_:)

Specifies a custom alignment anchor for a view that acts as a grid cell.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellAnchor(_ anchor: UnitPoint) -> some View
    

##  Parameters

`anchor`

    

The unit point that defines how to align the view within the bounds of its
grid cell.

## Return Value

A view that uses the specified anchor point to align its content.

## Discussion

Grids, like stacks and other layout containers, perform most alignment
operations using alignment guides. The grid moves the contents of each cell in
a row in the y direction until the specified `VerticalAlignment` guide of each
view in the row aligns with the same guide of all the other views in the row.
Similarly, the grid aligns the `HorizontalAlignment` guides of views in a
column by adjusting views in the x direction. See the guide types for more
information about typical SwiftUI alignment operations.

When you use the `gridCellAnchor(_:)` modifier on a view in a grid, the grid
changes to an anchor-based alignment strategy for the associated cell. With
anchor alignment, the grid projects a `UnitPoint` that you specify onto both
the view and the cell, and aligns the two projections. For example, consider
the following grid:

The grid creates red reference squares in the first row and column to
establish row and column sizes. Without the anchor modifier, the blue marker
in the remaining cell would appear at the center of its cell, because of the
grid’s default `center` alignment. With the anchor modifier shown in the code
above, the grid aligns the one quarter point of the marker with the one
quarter point of its cell in the x direction, as measured from the origin at
the top left of the cell. The grid also aligns the three quarters point of the
marker with the three quarters point of the cell in the y direction:

`UnitPoint` defines many convenience points that correspond to the typical
alignment guides, which you can use as well. For example, you can use
`topTrailing` to align the top and trailing edges of a view in a cell with the
top and trailing edges of the cell:

Applying the anchor-based alignment strategy to a single cell doesn’t affect
the alignment strategy that the grid uses on other cells.

### Anchor alignment for merged cells

If you use the `gridCellColumns(_:)` modifier to cause a cell to span more
than one column, or if you place a view in a grid outside of a row so that the
view spans the entire grid, the grid automatically converts its vertical and
horizontal alignment guides to the unit point equivalent for the merged cell,
and uses an anchor-based approach for that cell. For example, the following
grid places the marker at the center of the merged cell by converting the
grid’s default `center` alignment guide to a `center` anchor for the blue
marker in the merged cell:

The grid makes this conversion in part to avoid ambiguity. Each column has its
own horizontal guide, and it isn’t clear which of these a cell that spans
multiple columns should align with. Further, in the example above, neither of
the center alignment guides for the second or third column would provide the
expected behavior, which is to center the marker in the merged cell. Anchor
alignment provides this behavior:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellUnsizedAxes(_:)

Asks grid layouts not to offer the view extra size in the specified axes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellUnsizedAxes(_ axes: Axis.Set) -> some View
    

##  Parameters

`axes`

    

The dimensions in which the grid shouldn’t offer the view a share of any
available space. This prevents a flexible view like a `Spacer`, `Divider`, or
`Color` from defining the size of a row or column.

## Return Value

A view that doesn’t ask an enclosing grid for extra size in one or more axes.

## Discussion

Use this modifier to prevent a flexible view from taking more space on the
specified axes than the other cells in a row or column require. For example,
consider the following `Grid` that places a `Divider` between two rows of
content:

The text and images all have ideal widths for their content. However, because
a divider takes as much space as its parent offers, the grid fills the width
of the display, expanding all the other cells to match:

You can prevent the grid from giving the divider more width than the other
cells require by adding the modifier with the `Axis.horizontal` parameter:

This restores the grid to the width that it would have without the divider:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridColumnAlignment(_:)

Overrides the default horizontal alignment of the grid column that the view
appears in.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View
    

##  Parameters

`guide`

    

The `HorizontalAlignment` guide to use for the grid column that the view
appears in.

## Return Value

A view that uses the specified horizontal alignment, and that causes all cells
in the same column of a grid to use the same alignment.

## Discussion

You set a default alignment for the cells in a grid in both vertical and
horizontal dimensions when you create the grid with the
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer.
However, you can use the `gridColumnAlignment(_:)` modifier to override the
horizontal alignment of a column within the grid. The following example sets a
grid’s alignment to `leadingFirstTextBaseline`, and then sets the first column
to use `trailing` alignment:

This creates the layout of a typical macOS configuration view, with the
trailing edge of the first column flush with the leading edge of the second
column:

Add the modifier to only one cell in a column. The grid automatically aligns
all cells in that column the same way. You get undefined behavior if you apply
different alignments to different cells in the same column.

To override row alignment, see `init(alignment:content:)`. To override
alignment for a single cell, see `gridCellAnchor(_:)`.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

Instance Method

# ignoresSafeArea(_:edges:)

Expands the safe area of a view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func ignoresSafeArea(
        _ regions: SafeAreaRegions = .all,
        edges: Edge.Set = .all
    ) -> some View
    

##  Parameters

`regions`

    

The regions to expand the view’s safe area into. The modifier expands into all
safe area region types by default.

`edges`

    

The set of edges to expand. Any edges that you don’t include in this set
remain unchanged. The set includes all edges by default.

## Return Value

A view with an expanded safe area.

## Discussion

By default, the SwiftUI layout system sizes and positions views to avoid
certain safe areas. This ensures that system content like the software
keyboard or edges of the device don’t obstruct your views. To extend your
content into these regions, you can ignore safe areas on specific edges by
applying this modifier.

For examples of how to use this modifier, see Adding a background to your
view.

## See Also

### Staying in the safe areas

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaInset(edge:alignment:spacing:content:)

Shows the specified content beside the modified view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func safeAreaInset<V>(
        edge: HorizontalEdge,
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`edge`

    

The horizontal edge of the view to inset by the width of `content`, to make
space for `content`.

`spacing`

    

Extra distance placed between the two views, or nil to use the default amount
of spacing.

`alignment`

    

The alignment guide used to position `content` vertically.

`content`

    

A view builder function providing the view to display in the inset space of
the modified view.

## Return Value

A new view that displays `content` beside the modified view, making space for
the `content` view by horizontally insetting the modified view.

## Discussion

The `content` view is anchored to the specified horizontal edge in the parent
view, aligning its vertical axis to the specified alignment guide. The
modified view is inset by the width of `content`, from `edge`, with its safe
area increased by the same amount.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaInset(edge:alignment:spacing:content:)

Shows the specified content above or below the modified view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func safeAreaInset<V>(
        edge: VerticalEdge,
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`edge`

    

The vertical edge of the view to inset by the height of `content`, to make
space for `content`.

`spacing`

    

Extra distance placed between the two views, or nil to use the default amount
of spacing.

`alignment`

    

The alignment guide used to position `content` horizontally.

`content`

    

A view builder function providing the view to display in the inset space of
the modified view.

## Return Value

A new view that displays both `content` above or below the modified view,
making space for the `content` view by vertically insetting the modified view,
adjusting the safe area of the result to match.

## Discussion

The `content` view is anchored to the specified vertical edge in the parent
view, aligning its horizontal axis to the specified alignment guide. The
modified view is inset by the height of `content`, from `edge`, with its safe
area increased by the same amount.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(_ insets: EdgeInsets) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(_ length: CGFloat) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(Edge.Set, CGFloat?) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# safeAreaPadding(_:_:)

Adds the provided insets into the safe area of this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func safeAreaPadding(
        _ edges: Edge.Set = .all,
        _ length: CGFloat? = nil
    ) -> some View
    

## Discussion

Use this modifier when you would like to add a fixed amount of space to the
safe area a view sees.

See the `View/safeAreaInset(edge:alignment:spacing:content)` modifier for
adding to the safe area based on the size of a view.

## See Also

### Staying in the safe areas

`func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View`

Expands the safe area of a view.

`func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content beside the modified view.

`func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment,
spacing: CGFloat?, content: () -> V) -> some View`

Shows the specified content above or below the modified view.

`func safeAreaPadding(EdgeInsets) -> some View`

Adds the provided insets into the safe area of this view.

`func safeAreaPadding(CGFloat) -> some View`

Adds the provided insets into the safe area of this view.

`struct SafeAreaRegions`

A set of symbolic safe area regions.

Instance Method

# contentMargins(_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ length: CGFloat,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`length`

    

The amount of margins to add on all edges.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# contentMargins(_:_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ edges: Edge.Set = .all,
        _ length: CGFloat?,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`edges`

    

The edges to add the margins to.

`length`

    

The amount of margins to add.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, EdgeInsets, for: ContentMarginPlacement) ->
some View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# contentMargins(_:_:for:)

Configures the content margin for a provided placement.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func contentMargins(
        _ edges: Edge.Set = .all,
        _ insets: EdgeInsets,
        for placement: ContentMarginPlacement = .automatic
    ) -> some View
    

##  Parameters

`edges`

    

The edges to add the margins to.

`insets`

    

The amount of margins to add.

`placement`

    

Where the margins should be added.

## Discussion

Use this modifier to customize the content margins of different kinds of
views. For example, you can use this modifier to customize the margins of
scrollable views like `ScrollView`. In the following example, the scroll view
will automatically inset its content by the safe area plus an additional 20
points on the leading and trailing edge.

You can provide a `ContentMarginPlacement` to target specific parts of a view
to customize. For example, provide a `ContentMargingPlacement/scrollContent`
placement to inset the content of a `TextEditor` without affecting the insets
of its scroll indicators.

Similarly, you can customize the insets of scroll indicators separately from
scroll content. Consider doing this when applying a custom clip shape that may
clip the indicators.

When applying multiple contentMargins modifiers, modifiers with the same
placement will override modifiers higher up in the view hierarchy.

## See Also

### Setting margins

`func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View`

Configures the content margin for a provided placement.

`func contentMargins(Edge.Set, CGFloat?, for: ContentMarginPlacement) -> some
View`

Configures the content margin for a provided placement.

`struct ContentMarginPlacement`

The placement of margins.

Instance Method

# zIndex(_:)

Controls the display order of overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func zIndex(_ value: Double) -> some View
    

##  Parameters

`value`

    

A relative front-to-back ordering for this view; the default is `0`.

## Discussion

Use `zIndex(_:)` when you want to control the front-to-back ordering of views.

In this example there are two overlapping rotated rectangles. The frontmost is
represented by the larger index value.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# layoutDirectionBehavior(_:)

Sets the behavior of this view for different layout directions.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func layoutDirectionBehavior(_ behavior: LayoutDirectionBehavior) -> some View
    

##  Parameters

`behavior`

    

A LayoutDirectionBehavior value that indicates whether this view should mirror
in a particular layout direction. By default, views will adjust their layouts
automatically in a right-to-left context and do not need to be mirrored.

## Return Value

A view that conditionally mirrors its contents horizontally in a given layout
direction.

## Discussion

Use `layoutDirectionBehavior(_:)` when you need the system to horizontally
mirror the contents of the view when presented in a layout direction.

To override the layout direction for a specific view, use the
`environment(_:_:)` view modifier to explicitly override the `layoutDirection`
environment value for the view.

## See Also

### Setting a layout direction

`enum LayoutDirectionBehavior`

A description of what should happen when the layout direction changes.

`var layoutDirection: LayoutDirection`

The layout direction associated with the current environment.

`enum LayoutDirection`

A direction in which SwiftUI can lay out content.

Instance Method

# layoutValue(key:value:)

Associates a value with a custom layout property.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func layoutValue<K>(
        key: K.Type,
        value: K.Value
    ) -> some View where K : LayoutValueKey
    

##  Parameters

`key`

    

The type of the key that you want to set a value for. Create the key as a type
that conforms to the `LayoutValueKey` protocol.

`value`

    

The value to assign to the key for this view. The value must be of the type
that you establish for the key’s associated value when you implement the key’s
`defaultValue` property.

## Return Value

A view that has the specified value for the specified key.

## Discussion

Use this method to set a value for a custom property that you define with
`LayoutValueKey`. For example, if you define a `Flexibility` key, you can set
the key on a `Text` view using the key’s type and a value:

For convenience, you might define a method that does this in an extension to
`View`:

This method makes the call site easier to read:

If you perform layout operations in a type that conforms to the `Layout`
protocol, you can read the key’s associated value for each subview of your
custom layout type. Do this by indexing the subview’s proxy with the key. For
more information, see `LayoutValueKey`.

## See Also

### Associating values with views in a custom layout

`protocol LayoutValueKey`

A key for accessing a layout value of a layout container’s subviews.



# LabelStyle

Type Property

# automatic

A label style that resolves its appearance automatically based on the current
context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var automatic: DefaultLabelStyle { get }

Available when `Self` is `DefaultLabelStyle`.

## See Also

### Getting built-in label styles

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

Type Property

# iconOnly

A label style that only displays the icon of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var iconOnly: IconOnlyLabelStyle { get }

Available when `Self` is `IconOnlyLabelStyle`.

## Discussion

The title of the label is still used for non-visual descriptions, such as
VoiceOver.

## See Also

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

Type Property

# titleAndIcon

A label style that shows both the title and icon of the label using a system-
standard layout.

iOS 14.5+  iPadOS 14.5+  macOS 11.3+  Mac Catalyst 14.5+  tvOS 14.5+  watchOS
7.4+  visionOS 1.0+

    
    
    static var titleAndIcon: TitleAndIconLabelStyle { get }

Available when `Self` is `TitleAndIconLabelStyle`.

## Discussion

In most cases, labels show both their title and icon by default. However, some
containers might apply a different default label style to their content, such
as only showing icons within toolbars on macOS and iOS. To opt in to showing
both the title and the icon, you can apply the title and icon label style:

To apply the title and icon style to a group of labels, apply the style to the
view hierarchy that contains the labels:

The relative layout of the title and icon is dependent on the context it is
displayed in. In most cases, however, the label is arranged horizontally with
the icon leading.

## See Also

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleOnly: TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Available when `Self` is `TitleOnlyLabelStyle`.

Type Property

# titleOnly

A label style that only displays the title of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    static var titleOnly: TitleOnlyLabelStyle { get }

Available when `Self` is `TitleOnlyLabelStyle`.

## See Also

### Getting built-in label styles

`static var automatic: DefaultLabelStyle`

A label style that resolves its appearance automatically based on the current
context.

Available when `Self` is `DefaultLabelStyle`.

`static var iconOnly: IconOnlyLabelStyle`

A label style that only displays the icon of the label.

Available when `Self` is `IconOnlyLabelStyle`.

`static var titleAndIcon: TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

Available when `Self` is `TitleAndIconLabelStyle`.

Instance Method

# makeBody(configuration:)

Creates a view that represents the body of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    @ViewBuilder
    func makeBody(configuration: Self.Configuration) -> Self.Body

**Required**

##  Parameters

`configuration`

    

The properties of the label.

## Discussion

The system calls this method for each `Label` instance in a view hierarchy
where this style is the current label style.

## See Also

### Creating custom label styles

`typealias Configuration`

The properties of a label.

`associatedtype Body : View`

A view that represents the body of a label.

**Required**

Type Alias

# LabelStyle.Configuration

The properties of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    typealias Configuration = LabelStyleConfiguration

## See Also

### Creating custom label styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a label.

**Required**

` associatedtype Body : View`

A view that represents the body of a label.

**Required**

Associated Type

# Body

A view that represents the body of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    associatedtype Body : View

**Required**

## See Also

### Creating custom label styles

`func makeBody(configuration: Self.Configuration) -> Self.Body`

Creates a view that represents the body of a label.

**Required**

` typealias Configuration`

The properties of a label.

Structure

# DefaultLabelStyle

The default label style in the current context.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct DefaultLabelStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the label style

`init()`

Creates an automatic label style.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Structure

# IconOnlyLabelStyle

A label style that only displays the icon of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct IconOnlyLabelStyle

## Overview

You can also use `iconOnly` to construct this style.

## Topics

### Creating the label style

`init()`

Creates an icon-only label style.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Structure

# TitleAndIconLabelStyle

A label style that shows both the title and icon of the label using a system-
standard layout.

iOS 14.5+  iPadOS 14.5+  macOS 11.3+  Mac Catalyst 14.5+  tvOS 14.5+  watchOS
7.4+  visionOS 1.0+

    
    
    struct TitleAndIconLabelStyle

## Overview

You can also use `titleAndIcon` to construct this style.

## Topics

### Creating the label style

`init()`

Creates a label style that shows both the title and icon of the label using a
system-standard layout.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleOnlyLabelStyle`

A label style that only displays the title of the label.

Structure

# TitleOnlyLabelStyle

A label style that only displays the title of the label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct TitleOnlyLabelStyle

## Overview

You can also use `titleOnly` to construct this style.

## Topics

### Creating the label style

`init()`

Creates a title-only label style.

## Relationships

### Conforms To

  * `LabelStyle`

## See Also

### Supporting types

`struct DefaultLabelStyle`

The default label style in the current context.

`struct IconOnlyLabelStyle`

A label style that only displays the icon of the label.

`struct TitleAndIconLabelStyle`

A label style that shows both the title and icon of the label using a system-
standard layout.



# LongPressGesture

Initializer

# init(minimumDuration:)

Creates a long-press gesture with a minimum duration

tvOS 14.0+

    
    
    init(minimumDuration: Double = 0.5)

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

## See Also

### Creating a long press gesture

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

Initializer

# init(minimumDuration:maximumDistance:)

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    init(
        minimumDuration: Double = 0.5,
        maximumDistance: CGFloat = 10
    )

##  Parameters

`minimumDuration`

    

The minimum duration of the long press that must elapse before the gesture
succeeds.

`maximumDistance`

    

The maximum distance that the fingers or cursor performing the long press can
move before the gesture fails.

## See Also

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

Instance Property

# minimumDuration

The minimum duration of the long press that must elapse before the gesture
succeeds.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 14.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var minimumDuration: Double

## See Also

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var maximumDistance: CGFloat`

The maximum distance that the long press can move before the gesture fails.

Instance Property

# maximumDistance

The maximum distance that the long press can move before the gesture fails.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  watchOS 6.0+
visionOS 1.0+

    
    
    var maximumDistance: CGFloat { get set }

## See Also

### Creating a long press gesture

`init(minimumDuration: Double)`

Creates a long-press gesture with a minimum duration

`init(minimumDuration: Double, maximumDistance: CGFloat)`

Creates a long-press gesture with a minimum duration and a maximum distance
that the interaction can move before the gesture fails.

`var minimumDuration: Double`

The minimum duration of the long press that must elapse before the gesture
succeeds.



# List

Initializer

# init(content:)

Creates a list with the given content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init(@ViewBuilder content: () -> Content)

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

Initializer

# init(selection:content:)

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

macOS 13.0+

    
    
    @MainActor
    init(
        selection: Binding<SelectionValue>,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`selection`

    

A binding to a selected row.

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

Initializer

# init(selection:content:)

Creates a list with the given content that supports selecting a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @MainActor
    init(
        selection: Binding<SelectionValue?>?,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`selection`

    

A binding to a selected row.

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

Initializer

# init(selection:content:)

Creates a list with the given content that supports selecting multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init(
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder content: () -> Content
    )

##  Parameters

`selection`

    

A binding to a set that identifies selected rows.

`content`

    

The content of the list.

## See Also

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

Initializer

# init(_:rowContent:)

Creates a list that computes its views on demand over a constant range.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

macOS 13.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:selection:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, RowContent>, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:selection:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<RowContent>(
        _ data: Range<Int>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Int) -> RowContent
    ) where Content == ForEach<Range<Int>, Int, HStack<RowContent>>, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

A constant range of data to populate the list.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

This instance only reads the initial value of `data` and doesn’t need to
identify views across updates. To compute views on demand over a dynamic
range, use `init(_:id:selection:rowContent:)`.

## See Also

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, ID, RowContent>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
10.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == ForEach<Data, Data.Element.ID, RowContent>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:selection:rowContent:)

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, ID)>, ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+
visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<LazyMapSequence<Data.Indices, (Data.Index, Data.Element.ID)>, Data.Element.ID, RowContent>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Data,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Data,
        id: KeyPath<Data.Element, ID>,
        children: KeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Data.Element) -> RowContent
    ) where Content == OutlineGroup<Data, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:children:selection:rowContent:)

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The data for populating the list.

`id`

    

The key path to the data model’s identifier.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes a node capable of having children that is
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then `data` is treated as a
leaf node in the tree, like a regular file in a file system.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:children:selection:rowContent:)

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        children: WritableKeyPath<Data.Element, Data?>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == OutlineGroup<Binding<Data>, Data.Element.ID, RowContent, RowContent, DisclosureGroup<RowContent, OutlineSubgroupChildren>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`children`

    

A key path to a property whose non-`nil` value gives the children of `data`. A
non-`nil` but empty value denotes an element capable of having children that’s
currently childless, such as an empty directory in a file system. On the other
hand, if the property at the key path is `nil`, then the outline group treats
`data` as a leaf in the tree, like a regular file in a file system.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## See Also

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

macOS 13.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select a
single element.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select a
single elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, RowContent>(
        _ data: Binding<Data>,
        editActions: EditActions<Data>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, Data.Element.ID>, Data.Element.ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, RowContent : View, Data.Element : Identifiable, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing and to be edited by the list.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select
multiple elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

##  Parameters

`data`

    

A collection of identifiable data for computing the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        selection: Binding<Set<SelectionValue>>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing and to be edited by the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a set that identifies selected rows.

`rowContent`

    

A view builder that creates the view for a single row of

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select
multiple elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

macOS 13.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue>,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing and to be edited by the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a non optional selected value.

`rowContent`

    

A view builder that creates the view for a single row of

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and selects
a single row.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Initializer

# init(_:id:editActions:selection:rowContent:)

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  visionOS
1.0+

    
    
    @MainActor
    init<Data, ID, RowContent>(
        _ data: Binding<Data>,
        id: KeyPath<Data.Element, ID>,
        editActions: EditActions<Data>,
        selection: Binding<SelectionValue?>?,
        @ViewBuilder rowContent: @escaping (Binding<Data.Element>) -> RowContent
    ) where Content == ForEach<IndexedIdentifierCollection<Data, ID>, ID, EditableCollectionContent<RowContent, Data>>, Data : MutableCollection, Data : RandomAccessCollection, ID : Hashable, RowContent : View, Data.Index : Hashable

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

##  Parameters

`data`

    

The identifiable data for computing the list.

`id`

    

The key path to the data model’s identifier.

`editActions`

    

The edit actions that are synthesized on `data`.

`selection`

    

A binding to a selected value.

`rowContent`

    

A view builder that creates the view for a single row of the list.

## Discussion

The following example creates a list to display a collection of favorite foods
allowing the user to delete or move elements from the collection, and select a
single elements.

Use `deleteDisabled(_:)` and `moveDisabled(_:)` to disable respectively delete
or move actions on a per-row basis.

Explicit `DynamicViewContent.onDelete(perform:)`,
`DynamicViewContent.onMove(perform:)`, or
`View.swipeActions(edge:allowsFullSwipe:content:)` modifiers will override any
synthesized action

## See Also

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

Instance Property

# body

The content of the list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    var body: some View { get }



# LayoutProperties

Initializer

# init()

Creates a default set of properties.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init()

## Discussion

Use a layout properties instance to provide information about a type that
conforms to the `Layout` protocol. For example, you can create a layout
properties instance in your layout’s implementation of the `layoutProperties`
method, and use it to indicate that the layout has a `Axis.vertical`
orientation:

Instance Property

# stackOrientation

The orientation of the containing stack-like container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var stackOrientation: Axis?

## Discussion

Certain views alter their behavior based on the stack orientation of the
container that they appear in. For example, `Spacer` and `Divider` align their
major axis to match that of their container.

Set the orientation for your custom layout container by returning a configured
`LayoutProperties` instance from your `Layout` type’s implementation of the
`layoutProperties` method. For example, you can indicate that your layout has
a `Axis.vertical` major axis:

A value of `nil`, which is the default when you don’t specify a value,
indicates an unknown orientation, or that a layout isn’t one-dimensional.



# Lists

Article

# Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

## Overview

Displaying a collection of data in a vertical list is a common requirement in
many apps. Whether it’s a list of contacts, a schedule of events, an index of
categories, or a shopping list, you’ll often find a use for a `List`.

List views display collections of items vertically, load rows as needed, and
add scrolling when the rows don’t fit on the screen, making them suitable for
displaying large collections of data.

By default, list views also apply platform-appropriate styling to their
elements. For example, on iOS, the default configuration of a list displays a
separator line between each row, and adds disclosure indicators next to items
that initiate navigation actions.

Note

If you want to remove the platform-appropriate styling — such as row
separators or automatic disclosure indicators — from your list, consider using
`LazyVStack` instead. For more information on working with lazy stacks, see
Creating performant scrollable stacks

The code in this article shows the use of list views to display a company’s
staff directory. Each section enhances the usefulness of the list, by adding
custom cells, splitting the list into sections, and using the list selection
to navigate to a detail view.

### Prepare your data for iteration

The most common use of `List` is for representing collections of information
in your data model. The following example defines a `Person` as an
`Identifiable` type with the properties `name` and `phoneNumber`. An array
called `staff` contains two instances of this type.

To present the contents of the array as a list, the example creates a `List`
instance. The list’s content builder uses a `ForEach` to iterate over the
`staff` array. For each member of the array, the listing creates a row view by
instantiating a new `Text` that contains the name of the `Person`.

Members of a list must be uniquely identifiable from one another. Unique
identifiers allow SwiftUI to automatically generate animations for changes in
the underlying data, like inserts, deletions, and moves. Identify list members
either by using a type that conforms to `Identifiable`, as `Person` does, or
by providing an `id` parameter with the key path to a unique property of the
type. The `ForEach` that populates the list above depends on this behavior, as
do the `List` initializers that take a `RandomAccessCollection` of members to
iterate over.

Important

The values you use for `Identifiable` data must be unique. Using a `UUID` or a
database row identifier are both good choices, whereas using data like a
person’s name or phone number could potentially contain duplicates.

### Display data inside a row

Each row inside a `List` must be a SwiftUI `View`. You may be able to
represent your data with a single view such as an `Image` or `Text` view, or
you may need to define a custom view to compose several views into something
more complex.

As your row views get more sophisticated, refactor the views into separate
view structures, passing in the data that the row needs to render. The
following example defines a `PersonRowView` to create a two-line view for a
`Person`, using fonts, colors, and the system “phone” icon image to visually
style the data.

For more information on composing the types of views commonly used inside list
rows, see Building layouts with stack views.

### Represent data hierarchy with sections

`List` views can also display data with a level of hierarchy, grouping
associated data into sections.

Consider an expanded data model that represents an entire company, including
multiple departments. Each `Department` has a name and an array of `Person`
instances, and the company has an array of the `Department` type.

Use `Section` views to give the data inside a `List` a level of hierarchy.
Start by creating the `List`, using a `ForEach` to iterate over the
`company.departments` array, and then create `Section` views for each
department. Within the section’s view builder, use a `ForEach` to iterate over
the department’s `staff`, and return a customized view for each `Person`.

Note

If your data hierarchy is too deep to represent with a single level of
sections and rows, `OutlineGroup` and `DisclosureGroup` might be a better fit.
These views use a disclosure metaphor to allow the user to drill down to an
arbitrary depth in the hierarchy.

## Use Lists for Navigation

Using a `NavigationLink` within a `List` contained inside a `NavigationView`
adds platform-appropriate visual styling, and in some cases, additional
container views that provide the structure for navigation. SwiftUI uses one of
two visual presentations, based on the runtime environment:

  * A list with disclosure indicators, which performs an animated navigation to a destination scene when the user chooses a list item. SwiftUI uses this presentation on watchOS, tvOS, and on most iOS devices except as described below.

  * A two-panel split view, with the top-level data as a list on the left side and the detail on the right. To get this presentation, you also need to provide a placeholder view after the list; this placeholder fills the detail pane until the user makes a selection. SwiftUI uses this two-panel approach on macOS, iPadOS, and on iOS devices with sufficient horizontal space, as indicated by the `horizontalSizeClass` environment value.

The following example sets up a navigation-based UI by wrapping the list with
a navigation view. Instances of `NavigationLink` wrap the list’s rows to
provide a `destination` view to navigate to when the user taps the row. If a
split view navigation is appropriate for the platform, the right panel
initially contains the “No Selection” placeholder view, which the navigation
view replaces with the destination view when the user makes a selection.

In this example, the view passed in as the `destination` is a
`PersonDetailView`, which repeats the information from the list. In a more
complex app, this detail view could show more information about a `Person`
than would fit inside the list row.

On most iOS devices (those with a compact horizontal size class), the list
appears as a view by itself, and tapping a row performs an animated transition
to the destination view. The following figure shows both the list view and the
destination view that appears when the user makes a selection:

On the other hand, iPadOS and macOS show the list and the detail view together
as a multi-column view. The following figure shows what this example looks
like on macOS prior to making a selection, which means the “No selection”
placeholder view is still in the detail column.

You can use the `navigationViewStyle(_:)` view modifier to change the default
behavior of a `NavigationView`. For example, on iOS, the
`StackNavigationViewStyle` forces single-column mode, even on an iPad in
landscape orientation.

## See Also

### Creating a list

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Structure

# List

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @MainActor
    struct List<SelectionValue, Content> where SelectionValue : Hashable, Content : View

## Overview

In its simplest form, a `List` creates its contents statically, as shown in
the following example:

More commonly, you create lists dynamically from an underlying collection of
data. The following example shows how to create a simple list from an array of
an `Ocean` type which conforms to `Identifiable`:

### Supporting selection in lists

To make members of a list selectable, provide a binding to a selection
variable. Binding to a single instance of the list data’s `Identifiable.ID`
type creates a single-selection list. Binding to a `Set` creates a list that
supports multiple selections. The following example shows how to add
multiselect to the previous example:

When people make a single selection by tapping or clicking, the selected cell
changes its appearance to indicate the selection. To enable multiple
selections with tap gestures, put the list into edit mode by either modifying
the `editMode` value, or adding an `EditButton` to your app’s interface. When
you put the list into edit mode, the list shows a circle next to each list
item. The circle contains a checkmark when the user selects the associated
item. The example above uses an Edit button, which changes its title to Done
while in edit mode:

People can make multiple selections without needing to enter edit mode on
devices that have a keyboard and mouse or trackpad, like Mac and iPad.

### Refreshing the list content

To make the content of the list refreshable using the standard refresh
control, use the `refreshable(action:)` modifier.

The following example shows how to add a standard refresh control to a list.
When the user drags the top of the list downward, SwiftUI reveals the refresh
control and executes the specified action. Use an `await` expression inside
the `action` closure to refresh your data. The refresh indicator remains
visible for the duration of the awaited operation.

### Supporting multidimensional lists

To create two-dimensional lists, group items inside `Section` instances. The
following example creates sections named after the world’s oceans, each of
which has `Text` views named for major seas attached to those oceans. The
example also allows for selection of a single list item, identified by the
`id` of the example’s `Sea` type.

Because this example uses single selection, people can make selections outside
of edit mode on all platforms.

Note

In iOS 15, iPadOS 15, and tvOS 15 and earlier, lists support selection only in
edit mode, even for single selections.

### Creating hierarchical lists

You can also create a hierarchical list of arbitrary depth by providing tree-
structured data and a `children` parameter that provides a key path to get the
child nodes at any level. The following example uses a deeply-nested
collection of a custom `FileItem` type to simulate the contents of a file
system. The list created from this data uses collapsing cells to allow the
user to navigate the tree structure.

### Styling lists

SwiftUI chooses a display style for a list based on the platform and the view
type in which it appears. Use the `listStyle(_:)` modifier to apply a
different `ListStyle` to all lists within a view. For example, adding
`.listStyle(.plain)` to the example shown in the “Creating Multidimensional
Lists” topic applies the `plain` style, the following screenshot shows:

## Topics

### Creating a list with arbitrary content

`init(content: () -> Content)`

Creates a list with the given content.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init(selection: Binding<SelectionValue>, content: () -> Content)`

Creates a list with the given content that supports selecting a single row
that cannot be deselcted.

`init(selection: Binding<SelectionValue?>?, content: () -> Content)`

Creates a list with the given content that supports selecting a single row.

`init(selection: Binding<Set<SelectionValue>>?, content: () -> Content)`

Creates a list with the given content that supports selecting multiple rows.

### Creating a list from a range

`init<RowContent>(Range<Int>, rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue>, rowContent:
(Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range and
allowing users to have exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<SelectionValue?>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<RowContent>(Range<Int>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Int) -> RowContent)`

Creates a list that computes its views on demand over a constant range,
optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<SelectionValue?>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Data.Element) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing identifiable data

`init<Data, RowContent>(Data, rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allowing users to have exactly one row always
selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing bound data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that identifies its rows based on a key path to the identifier
of the underlying data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing bound, identifiable data

`init<Data, RowContent>(Binding<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, optionally allowing users to select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing hierarchical data

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue?>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue>, rowContent: (Data.Element) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data and allowing users to have exactly
one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<SelectionValue?>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Data, children: KeyPath<Data.Element, Data?>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Data.Element) ->
RowContent)`

Creates a hierarchical list that computes its rows on demand from an
underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing bound, hierarchical data

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Data, id: KeyPath<Data.Element, ID>, children:
KeyPath<Data.Element, Data?>, selection: Binding<SelectionValue>, rowContent:
(Data.Element) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data and allowing users to have exactly one
row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
children: WritableKeyPath<Data.Element, Data?>, selection:
Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a hierarchical list that identifies its rows based on a key path to
the identifier of the underlying data, optionally allowing users to select
multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue>, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data and allowing users to have
exactly one row always selected.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<SelectionValue?>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, children: WritableKeyPath<Data.Element,
Data?>, selection: Binding<Set<SelectionValue>>?, rowContent:
(Binding<Data.Element>) -> RowContent)`

Creates a hierarchical list that computes its rows on demand from a binding to
an underlying collection of identifiable data, optionally allowing users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Listing editable data

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and requires a selection
of a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<SelectionValue?>?, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, RowContent>(Binding<Data>, editActions: EditActions<Data>,
selection: Binding<Set<SelectionValue>>?, rowContent: (Binding<Data.Element>)
-> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, rowContent: (Binding<Data.Element>) ->
RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data and allows to edit the collection.

Available when `SelectionValue` is `Never` and `Content` conforms to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<Set<SelectionValue>>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and optionally allows users to
select multiple rows.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue>,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable, allows to edit the collection, and requires a selection of a
single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

`init<Data, ID, RowContent>(Binding<Data>, id: KeyPath<Data.Element, ID>,
editActions: EditActions<Data>, selection: Binding<SelectionValue?>?,
rowContent: (Binding<Data.Element>) -> RowContent)`

Creates a list that computes its rows on demand from an underlying collection
of identifiable data, allows to edit the collection, and optionally allowing
users to select a single row.

Available when `SelectionValue` conforms to `Hashable` and `Content` conforms
to `View`.

### Supporting types

`var body: some View`

The content of the list.

## Relationships

### Conforms To

  * `View`

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Instance Method

# listStyle(_:)

Sets the style for lists within this view.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listStyle<S>(_ style: S) -> some View where S : ListStyle
    

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`struct Section`

A container view that you can use to add hierarchy within certain views.

Structure

# Section

A container view that you can use to add hierarchy within certain views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Section<Parent, Content, Footer>

## Overview

Use `Section` instances in views like `List`, `Picker`, and `Form` to organize
content into separate sections. Each section has custom content that you
provide on a per-instance basis. You can also provide headers and footers for
each section.

### Collapsible sections

Create sections that expand and collapse by using an initializer that accepts
an `isExpanded` binding. A collapsible section in a `List` that uses the
`sidebar` style shows a disclosure indicator next to the section’s header.
Tapping on the disclosure indicator toggles the appearance of the section’s
content.

Note

Not all contexts provide a default control to trigger collapse or expansion.

## Topics

### Creating a section

`init<V>(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init<S>(S, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init<V, S>(S, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init<V>(LocalizedStringKey, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

### Adding headers and footers

`init(content: () -> Content, header: () -> Parent)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init<V, H>(content: () -> Content, header: () -> H)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init(content: () -> Content, footer: () -> Footer)`

Creates a section with a footer and the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

`init(content: () -> Content, header: () -> Parent, footer: () -> Footer)`

Creates a section with a header, footer, and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

### Controlling collapsibility

`init<V, S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init<V>(LocalizedStringKey, isExpanded: Binding<Bool>, content: () ->
Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

`init(isExpanded: Binding<Bool>, content: () -> Content, header: () ->
Parent)`

Creates a section with a header, the provided section content, and a binding
representing the section’s expansion state.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init<V, H>(isExpanded: Binding<Bool>, content: () -> Content, header: () ->
H)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

### Deprecated symbols

`init(header: Parent, content: () -> Content)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

Deprecated

`init(footer: Footer, content: () -> Content)`

Creates a section with a footer and the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

`init(header: Parent, footer: Footer, content: () -> Content)`

Creates a section with a header, footer, and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

`func collapsible(Bool) -> some View`

Sets whether a section can be collapsed by the user.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

## Relationships

### Conforms To

  * `TableRowContent`

Conforms when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

  * `View`

Conforms when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

## See Also

### Creating a list

Displaying data in lists

Visualize collections of data with platform-appropriate appearance.

`struct List`

A container that presents rows of data arranged in a single column, optionally
providing the ability to select one or more members.

`func listStyle<S>(S) -> some View`

Sets the style for lists within this view.

Structure

# ForEach

A structure that computes views on demand from an underlying collection of
identified data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct ForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable

## Overview

Use `ForEach` to provide views based on a `RandomAccessCollection` of some
data type. Either the collection’s elements must conform to `Identifiable` or
you need to provide an `id` parameter to the `ForEach` initializer.

The following example creates a `NamedFont` type that conforms to
`Identifiable`, and an array of this type called `namedFonts`. A `ForEach`
instance iterates over the array, producing new `Text` instances that display
examples of each SwiftUI `Font` style provided in the array.

## Topics

### Creating a collection from a range

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes views on demand over a given constant range.

Available when `Data` is `Range<Int>`, `ID` is `Int`, and `Content` conforms
to `View`.

### Creating a collection from data

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `View`, and `Data.Element` conforms
to `Identifiable`.

`init<C>(Binding<C>, content: (Binding<C.Element>) -> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init<C>(Binding<C>, id: KeyPath<C.Element, ID>, content: (Binding<C.Element>)
-> Content)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

`init(Data)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

### Generating rotor content

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AccessibilityRotorContent`, and
`Data.Element` conforms to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that generates Rotor content by combining, in order,
individual Rotor content for each element in the data given to this `ForEach`.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

### Creating a collection of table rows

`init<V>(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes table rows on demand over a given constant
range.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

`init<V>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates table rows across
updates based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

### Creating chart content

`init(Data, content: (Data.Element) -> Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `ChartContent`, and `Data.Element`
conforms to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `ChartContent`.

### Creating editable content

`init<C, R>(Binding<C>, editActions: EditActions<C>, content:
(Binding<C.Element>) -> R)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

`init<C, R>(Binding<C>, id: KeyPath<C.Element, ID>, editActions:
EditActions<C>, content: (Binding<C.Element>) -> R)`

Creates an instance that uniquely identifies and creates views across updates
based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection` and `ID` conforms
to `Hashable`.

### Creating attachment content

`init(Data, content: (Data.Element) -> Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Content` conforms to `AttachmentContent`, and
`Data.Element` conforms to `Identifiable`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AttachmentContent`.

### Accessing content

`var content: (Data.Element) -> Content`

A function to create content on demand using the underlying data.

`var data: Data`

The collection of underlying identified data that SwiftUI uses to create views
dynamically.

### Initializers

`init(Range<Int>, content: (Int) -> Content)`

Creates an instance that computes map content on demand over a given constant
range.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

`init(Data, content: (Data.Element) -> Content)`

Creates an instance that uniquely identifies and creates map content across
updates based on the identity of the underlying data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

`init(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) ->
Content)`

Creates an instance that uniquely identifies and creates map content across
updates based on the provided key path to the underlying data’s identifier.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `MapContent`.

### Type Aliases

`typealias Body`

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

### Default Implementations

API Reference

AttachmentContent Implementations

API Reference

MapContent Implementations

## Relationships

### Conforms To

  * `AccessibilityRotorContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

  * `AttachmentContent`
  * `ChartContent`
  * `DynamicMapContent`
  * `DynamicTableRowContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

  * `DynamicViewContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

  * `MapContent`
  * `TableRowContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `TableRowContent`.

  * `View`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

## See Also

### Iterating over list content

`protocol DynamicViewContent`

A type of view that generates views from an underlying collection of data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

Protocol

# DynamicViewContent

A type of view that generates views from an underlying collection of data.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    protocol DynamicViewContent : View

## Topics

### Managing the data

`var data: Self.Data`

The collection of underlying data.

**Required**

` associatedtype Data : Collection`

The type of the underlying collection of data.

**Required**

### Responding to updates

`func onDelete(perform: Optional<(IndexSet) -> Void>) -> some
DynamicViewContent`

Sets the deletion action for the dynamic view.

`func onInsert(of: [UTType], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

`func onMove(perform: Optional<(IndexSet, Int) -> Void>) -> some
DynamicViewContent`

Sets the move action for the dynamic view.

`func dropDestination<T>(for: T.Type, action: ([T], Int) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

### Deprecated symbols

`func onInsert(of: [String], perform: (Int, [NSItemProvider]) -> Void) -> some
DynamicViewContent`

Sets the insert action for the dynamic view.

Deprecated

## Relationships

### Inherits From

  * `View`

### Conforming Types

  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

  * `ModifiedContent`

Conforms when `Content` conforms to `DynamicViewContent` and `Modifier`
conforms to `ViewModifier`.

## See Also

### Iterating over list content

`struct ForEach`

A structure that computes views on demand from an underlying collection of
identified data.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `View`.

Structure

# OutlineGroup

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct OutlineGroup<Data, ID, Parent, Leaf, Subgroup> where Data : RandomAccessCollection, ID : Hashable

## Overview

Use an outline group when you need a view that can represent a hierarchy of
data by using disclosure views. This allows the user to navigate the tree
structure by using the disclosure views to expand and collapse branches.

In the following example, a tree structure of `FileItem` data offers a
simplified view of a file system. Passing the root of this tree and the key
path of its children allows you to quickly create a visual representation of
the file system.

### Type parameters

Five generic type constraints define a specific `OutlineGroup` instance:

  * `Data`: The type of a collection containing the children of an element in the tree-shaped data.

  * `ID`: The type of the identifier for an element.

  * `Parent`: The type of the visual representation of an element whose children property is non-`nil`

  * `Leaf`: The type of the visual representation of an element whose children property is `nil`.

  * `Subgroup`: A type of a view that groups a parent view and a view representing its children, typically with some mechanism for showing and hiding the children

## Topics

### Creating an outline group

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, the key path to its
identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, the key path
to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

### Creating an outline group from a binding

`init<C, E>(Binding<E>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element and a key path
to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<C>, children: WritableKeyPath<E, C?>, content:
(Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements
and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `View`, `Parent` is `Leaf`, `Subgroup`
is `DisclosureGroup<Parent, OutlineSubgroupChildren>`, and `Data.Element`
conforms to `Identifiable`.

`init<C, E>(Binding<E>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a root data element, the key path
to its identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

`init<C, E>(Binding<C>, id: KeyPath<E, ID>, children: WritableKeyPath<E, C?>,
content: (Binding<E>) -> Leaf)`

Creates an outline group from a binding to a collection of root data elements,
the key path to a data element’s identifier, and a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Parent` is `Leaf`, and `Subgroup` is
`DisclosureGroup<Parent, OutlineSubgroupChildren>`.

### Creating an outline group in a table

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(Data, children: KeyPath<DataElement, Data?>, content:
(DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements and a key
path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, children: KeyPath<DataElement, Data?>,
content: (DataElement) -> Leaf)`

Creates an outline group from a root data element and a key path to its
children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

`init<DataElement>(DataElement, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a root data element, a key path to the its
identifier, as well as a key path to its children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

### Supporting types

`struct OutlineSubgroupChildren`

A type-erased view representing the children in an outline subgroup.

### Initializers

`init<DataElement>(Data, id: KeyPath<DataElement, ID>, children:
KeyPath<DataElement, Data?>, content: (DataElement) -> Leaf)`

Creates an outline group from a collection of root data elements, a key path
to the element’s identifier, as well as a key path to element’s children.

Available when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

## Relationships

### Conforms To

  * `TableRowContent`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` is
`Data.Element.ID`, `Parent` conforms to `TableRowContent`, `Parent` is `Leaf`,
`Leaf` is `Subgroup`, and `Data.Element` is `Parent.TableRowValue`.

  * `View`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, `Parent` conforms to `View`, `Leaf` conforms to `View`, and
`Subgroup` conforms to `View`.

## See Also

### Disclosing information progressively

`struct DisclosureGroup`

A view that shows or hides another content view, based on the state of a
disclosure control.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

Structure

# DisclosureGroup

A view that shows or hides another content view, based on the state of a
disclosure control.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct DisclosureGroup<Label, Content> where Label : View, Content : View

## Overview

A disclosure group view consists of a label to identify the contents, and a
control to show and hide the contents. Showing the contents puts the
disclosure group into the “expanded” state, and hiding them makes the
disclosure group “collapsed”.

In the following example, a disclosure group contains two toggles and an
embedded disclosure group. The top level disclosure group exposes its expanded
state with the bound property, `topLevelExpanded`. By expanding the disclosure
group, the user can use the toggles to update the state of the `toggleStates`
structure.

## Topics

### Creating a group with a string label

`init<S>(S, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(LocalizedStringKey, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided localized string key to create a
text view for the label, and a binding to the expansion state (expanded or
collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a disclosure group, using a provided string to create a text view for
the label, and a binding to the expansion state (expanded or collapsed).

Available when `Label` is `Text` and `Content` conforms to `View`.

### Creating a group with a label view

`init(content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views.

`init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)`

Creates a disclosure group with the given label and content views, and a
binding to the expansion state (expanded or collapsed).

## Relationships

### Conforms To

  * `View`

## See Also

### Disclosing information progressively

`struct OutlineGroup`

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

`func disclosureGroupStyle<S>(S) -> some View`

Sets the style for disclosure groups within this view.

Instance Method

# disclosureGroupStyle(_:)

Sets the style for disclosure groups within this view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func disclosureGroupStyle<S>(_ style: S) -> some View where S : DisclosureGroupStyle
    

## See Also

### Disclosing information progressively

`struct OutlineGroup`

A structure that computes views and disclosure groups on demand from an
underlying collection of tree-structured, identified data.

`struct DisclosureGroup`

A view that shows or hides another content view, based on the state of a
disclosure control.

Instance Method

# listRowInsets(_:)

Applies an inset to the rows in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowInsets(_ insets: EdgeInsets?) -> some View
    

##  Parameters

`insets`

    

The `EdgeInsets` to apply to the edges of the view.

## Return Value

A view that uses the given edge insets when used as a list cell.

## Discussion

Use `listRowInsets(_:)` to change the default padding of the content of list
items.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowInsets(_:)`
modifier then changes the edge insets of each row of the list according to the
`EdgeInsets` provided:

## See Also

### Configuring rows

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listRowHoverEffect(_:)

Requests that the containing list row use the provided hover effect.

visionOS 1.0+

    
    
    func listRowHoverEffect(_ effect: HoverEffect?) -> some View
    

##  Parameters

`effect`

    

The hover effect applied to the entire list row.

## Return Value

A view that requests a hover effect for a containing list row

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to change the default hover effect.

This modifier can be applied to a list row’s content to request that the list
row’s default effect be replaced by the provided effect. If the view is not
contained within a `List` or if the view does not support hover effects in
this context, the modifier has no effect.

Use a `nil` effect to indicate that the list row’s default hover effect should
not be modified.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listRowHoverEffectDisabled(_:)

Requests that the containing list row have its hover effect disabled.

visionOS 1.0+

    
    
    func listRowHoverEffectDisabled(_ disabled: Bool = true) -> some View
    

##  Parameters

`disabled`

    

A Boolean value that determines whether the containing list row should display
its default hover effect.

## Return Value

A view that requests the default hover effect on its containing list row to
conditionally be disabled.

## Discussion

By default, `List` rows have built-in hover effects in visionOS. In some
cases, it is useful to disable the default hover effect.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listItemTint(_:)

Sets a fixed tint color for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: Color?) -> some View
    

##  Parameters

`tint`

    

The color to use to tint the content. Use `nil` to avoid overriding the
inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

Note

This modifier is equivalent to using the version of the modifier that takes a
`ListItemTint` value and specifying the `tint` color in the corresponding
`fixed(_:)` input.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Method

# listItemTint(_:)

Sets the tint effect for content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    func listItemTint(_ tint: ListItemTint?) -> some View
    

##  Parameters

`tint`

    

The tint effect to use. Use `nil` to avoid overriding the inherited tint.

## Discussion

The containing list’s style applies the tint as appropriate. For example,
watchOS uses the tint color for its background platter appearance. Sidebars on
iOS and macOS apply the tint color to their `Label` icons, which otherwise use
the accent color by default.

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Structure

# ListItemTint

A tint effect configuration that you can apply to content in a list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct ListItemTint

## Overview

Use one of these tint values with the `listItemTint(_:)` view modifier. The
containing list applies the tint in a platform-specific way.

## Topics

### Getting list item tint options

`static let monochrome: ListItemTint`

A standard grayscale tint effect.

`static func fixed(Color) -> ListItemTint`

An explicit tint color.

`static func preferred(Color) -> ListItemTint`

An explicit tint color that the system can override.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`var defaultMinListRowHeight: CGFloat`

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

Instance Property

# defaultMinListRowHeight

The default minimum height of a row in a `List`. The default minimum height of
a row in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var defaultMinListRowHeight: CGFloat { get set }

## See Also

### Configuring rows

`func listRowInsets(EdgeInsets?) -> some View`

Applies an inset to the rows in a list.

`func listRowHoverEffect(HoverEffect?) -> some View`

Requests that the containing list row use the provided hover effect.

`func listRowHoverEffectDisabled(Bool) -> some View`

Requests that the containing list row have its hover effect disabled.

`func listItemTint(Color?) -> some View`

Sets a fixed tint color for content in a list.

`func listItemTint(ListItemTint?) -> some View`

Sets the tint effect for content in a list.

`struct ListItemTint`

A tint effect configuration that you can apply to content in a list.

Instance Method

# listRowSeparatorTint(_:edges:)

Sets the tint color associated with a row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the row separators, or `nil` to use the default color
for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose row separators are
tinted based on row-specific data:

To hide a row separators, use `listRowSeparator(_:edges:)`. To hide or change
the tint color for a section separator, use `listSectionSeparator(_:edges:)`
and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparatorTint(_:edges:)

Sets the tint color associated with a section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparatorTint(
        _ color: Color?,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`color`

    

The color to use to tint the section separators, or `nil` to use the default
color for the current list style.

`edges`

    

The set of row edges for which the tint applies. The list style might decide
to not display certain separators, typically the top edge. The default is
`all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter for the separator tint.

The following example shows a simple grouped list whose section separators are
tinted based on section-specific data:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To hide a
section separator, use `listSectionSeparator(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listRowSeparator(_:edges:)

Sets the display mode for the separator associated with this specific row.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this row’s separators.

`edges`

    

The set of row edges for which this preference applies. The list style might
already decide to not display separators for some edges, typically the top
edge. The default is `all`.

## Discussion

Separators can be presented above and below a row. You can specify to which
edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose row separators are
hidden:

To change the color of a row separators, use `listRowSeparatorTint(_:edges:)`.
To hide or change the tint color for a section separators, use
`listSectionSeparator(_:edges:)` and `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listSectionSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets whether to hide the separator associated with a list section.

Instance Method

# listSectionSeparator(_:edges:)

Sets whether to hide the separator associated with a list section.

iOS 15.0+  iPadOS 15.0+  macOS 13.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listSectionSeparator(
        _ visibility: Visibility,
        edges: VerticalEdge.Set = .all
    ) -> some View
    

##  Parameters

`visibility`

    

The visibility of this section’s separators.

`edges`

    

The set of row edges for which the preference applies. The list style might
already decide to not display separators for some edges. The default is `all`.

## Discussion

Separators can be presented above and below a section. You can specify to
which edge this preference should apply.

This modifier expresses a preference to the containing `List`. The list style
is the final arbiter of the separator visibility.

The following example shows a simple grouped list whose bottom sections
separator are hidden:

To change the visibility and tint color for a row separator, use
`listRowSeparator(_:edges:)` and `listRowSeparatorTint(_:edges:)`. To set the
tint color for a section separator, use `listSectionSeparatorTint(_:edges:)`.

## See Also

### Configuring separators

`func listRowSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a row.

`func listSectionSeparatorTint(Color?, edges: VerticalEdge.Set) -> some View`

Sets the tint color associated with a section.

`func listRowSeparator(Visibility, edges: VerticalEdge.Set) -> some View`

Sets the display mode for the separator associated with this specific row.

Instance Method

# headerProminence(_:)

Sets the header prominence for this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func headerProminence(_ prominence: Prominence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply.

## Discussion

In the following example, the section header appears with increased
prominence:

## See Also

### Configuring headers

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Property

# headerProminence

The prominence to apply to section headers within a view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var headerProminence: Prominence { get set }

## Discussion

The default is `Prominence.standard`.

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Enumeration

# Prominence

A type indicating the prominence of a view hierarchy.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    enum Prominence

## Topics

### Getting prominence options

`case standard`

The standard prominence.

`case increased`

An increased prominence.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`var defaultMinListHeaderHeight: CGFloat?`

The default minimum height of a header in a list.

Instance Property

# defaultMinListHeaderHeight

The default minimum height of a header in a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    var defaultMinListHeaderHeight: CGFloat? { get set }

## Discussion

When this value is `nil`, the system chooses the appropriate height. The
default is `nil`.

## See Also

### Configuring headers

`func headerProminence(Prominence) -> some View`

Sets the header prominence for this view.

`var headerProminence: Prominence`

The prominence to apply to section headers within a view.

`enum Prominence`

A type indicating the prominence of a view hierarchy.

Instance Method

# listRowSpacing(_:)

Sets the vertical spacing between two adjacent rows in a List.

iOS 15.0+  iPadOS 15.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func listRowSpacing(_ spacing: CGFloat?) -> some View
    

##  Parameters

`spacing`

    

The spacing value to use. A value of `nil` uses the default spacing.

## Discussion

The following example creates a List with 10 pts of spacing between each row:

## See Also

### Configuring spacing

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing to a custom value between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: CGFloat) -> some View
    

##  Parameters

`spacing`

    

the amount of spacing to apply.

## Discussion

The following example creates a List with 5 pts of spacing between sections:

Spacing can also be specified on a per-section basis. The following example
creates a List with compact spacing for its second section:

If adjacent sections have different spacing value, the smaller value on the
shared edge is used. Spacing specified inside the List is preferred over any
List-wide value.

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Instance Method

# listSectionSpacing(_:)

Sets the spacing between adjacent sections in a List.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    func listSectionSpacing(_ spacing: ListSectionSpacing) -> some View
    

## Discussion

Pass `.default` for the default spacing, or use `.compact` for a compact
appearance between sections.

The following example creates a List with compact spacing between sections:

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`struct ListSectionSpacing`

The spacing options between two adjacent sections in a list.

Structure

# ListSectionSpacing

The spacing options between two adjacent sections in a list.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    struct ListSectionSpacing

## Topics

### Getting section spacing

`static let `default`: ListSectionSpacing`

The default spacing between sections

`static let compact: ListSectionSpacing`

Compact spacing between sections

`static func custom(CGFloat) -> ListSectionSpacing`

Creates a custom spacing value.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Configuring spacing

`func listRowSpacing(CGFloat?) -> some View`

Sets the vertical spacing between two adjacent rows in a List.

`func listSectionSpacing(CGFloat) -> some View`

Sets the spacing to a custom value between adjacent sections in a List.

`func listSectionSpacing(ListSectionSpacing) -> some View`

Sets the spacing between adjacent sections in a List.

Instance Method

# listRowBackground(_:)

Places a custom background view behind a list row item.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func listRowBackground<V>(_ view: V?) -> some View where V : View
    

##  Parameters

`view`

    

The `View` to use as the background behind the list row view.

## Return Value

A list row view with `view` as its background view.

## Discussion

Use `listRowBackground(_:)` to place a custom background view behind a list
row item.

In the example below, the `Flavor` enumeration provides content for list
items. The SwiftUI `ForEach` structure computes views for each element of the
`Flavor` enumeration and extracts the raw value of each of its elements using
the resulting text to create each list row item. The `listRowBackground(_:)`
modifier then places the view you supply behind each of the list row items:

## See Also

### Configuring backgrounds

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Method

# alternatingRowBackgrounds(_:)

Overrides whether lists and tables in this view have alternating row
backgrounds.

macOS 14.0+

    
    
    func alternatingRowBackgrounds(_ behavior: AlternatingRowBackgroundBehavior = .enabled) -> some View
    

##  Parameters

`behavior`

    

Whether alternating row backgrounds are enabled or not.

## Discussion

This can be used in conjunction with an explicit list or table style or used
by itself to customize the row backgrounds of the automatic style. The only
list style this has no effect on is `.sidebar.`

This is able to be combined with `scrollContentBackground(_:)` and applies an
alternating row background on top of the overall list or table background.

This can also be combined with `listRowBackground`, which overrides the
background for a specific list row, replacing the automatic alternating
background for that row.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Structure

# AlternatingRowBackgroundBehavior

The styling of views with respect to alternating row backgrounds.

macOS 14.0+

    
    
    struct AlternatingRowBackgroundBehavior

## Overview

Use values of this type with the `alternatingRowBackgrounds(_:)` modifier.

## Topics

### Getting alternating row background behavior

`static let automatic: AlternatingRowBackgroundBehavior`

The automatic alternating row background behavior.

`static let enabled: AlternatingRowBackgroundBehavior`

Alternating rows will be enabled for applicable views.

`static let disabled: AlternatingRowBackgroundBehavior`

Alternating rows will be disabled for applicable views.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Instance Property

# backgroundProminence

The prominence of the background underneath views associated with this
environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    var backgroundProminence: BackgroundProminence { get set }

## Discussion

Foreground elements above an increased prominence background are typically
adjusted to have higher contrast against a potentially vivid color, such as
taking on a higher opacity monochrome appearance according to the
`colorScheme`. System styles like `primary`, `secondary`, etc will
automatically resolve to an appropriate style in this context. The property
can be read and used for custom styled elements.

In the example below, a custom star rating element is in a list row alongside
some text. When the row is selected and has an increased prominence
appearance, the text and star rating will update their appearance, the star
rating replacing its use of yellow with the standard `secondary` style.

Note that the use of `backgroundProminence` was used by a view that was nested
in additional stack containers within the row. This ensured that the value
correctly reflected the environment within the list row itself, as opposed to
the environment of the list as a whole. One way to ensure correct resolution
would be to prefer using this in a custom ShapeStyle instead, for example:

Views like `List` and `Table` as well as standard shape styles like
`ShapeStyle.selection` will automatically update the background prominence of
foreground views. For custom backgrounds, this environment property can be
explicitly set on views above custom backgrounds.

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`struct BackgroundProminence`

The prominence of backgrounds underneath other views.

Structure

# BackgroundProminence

The prominence of backgrounds underneath other views.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct BackgroundProminence

## Overview

Background prominence should influence foreground styling to maintain
sufficient contrast against the background. For example, selected rows in a
`List` and `Table` can have increased prominence backgrounds with accent color
fills when focused; the foreground content above the background should be
adjusted to reflect that level of prominence.

This can be read and written for views with the
`EnvironmentValues.backgroundProminence` property.

## Topics

### Getting background prominence

`static let standard: BackgroundProminence`

The standard prominence of a background

`static let increased: BackgroundProminence`

A more prominent background that likely requires some changes to the views
above it.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Configuring backgrounds

`func listRowBackground<V>(V?) -> some View`

Places a custom background view behind a list row item.

`func alternatingRowBackgrounds(AlternatingRowBackgroundBehavior) -> some
View`

Overrides whether lists and tables in this view have alternating row
backgrounds.

`struct AlternatingRowBackgroundBehavior`

The styling of views with respect to alternating row backgrounds.

`var backgroundProminence: BackgroundProminence`

The prominence of the background underneath views associated with this
environment.

Instance Method

# badge(_:)

Generates a badge for the view from a text view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ label: Text?) -> some View
    

##  Parameters

`label`

    

An optional `Text` view to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

Use this initializer when you want to style a `Text` view for use as a badge.
The following example customizes the badge with the `monospacedDigit()`,
`foregroundColor(_:)`, and `bold()` modifiers.

Styling the text view has no effect when the badge appears in a `TabView`.

## See Also

### Displaying a badge on a list item

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a string.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge<S>(_ label: S?) -> some View where S : StringProtocol
    

##  Parameters

`label`

    

An optional string to display as a badge. Set the value to `nil` to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:)`. The following example shows a list with a “Default”
badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from a localized string key.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ key: LocalizedStringKey?) -> some View
    

##  Parameters

`key`

    

An optional string key to display as a badge. Set the value to `nil` to hide
the badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

This modifier creates a `Text` view on your behalf, and treats the localized
key similar to `init(_:tableName:bundle:comment:)`. For more information about
localizing strings, see `Text`. The following example shows a list with a
“Default” badge on one of its rows.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badge(_:)

Generates a badge for the view from an integer value.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  visionOS 1.0+

    
    
    func badge(_ count: Int) -> some View
    

##  Parameters

`count`

    

An integer value to display in the badge. Set the value to zero to hide the
badge.

## Discussion

Use a badge to convey optional, supplementary information about a view. Keep
the contents of the badge as short as possible. Badges appear only in list
rows, tab bars, and menus.

The following example shows a `List` with the value of `recentItems.count`
represented by a badge on one of the rows:

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Method

# badgeProminence(_:)

Specifies the prominence of badges created by this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func badgeProminence(_ prominence: BadgeProminence) -> some View
    

##  Parameters

`prominence`

    

The prominence to apply to badges.

## Discussion

Badges can be used for different kinds of information, from the passive number
of items in a container to the number of required actions. The prominence of
badges in Lists can be adjusted to reflect this and be made to draw more or
less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an
informational badge with lower prominence, showing the number of items in the
folder.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

`struct BadgeProminence`

The visual prominence of a badge.

Instance Property

# badgeProminence

The prominence to apply to badges associated with this environment.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    var badgeProminence: BadgeProminence { get set }

## Discussion

The default is `standard`.

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`struct BadgeProminence`

The visual prominence of a badge.

Structure

# BadgeProminence

The visual prominence of a badge.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    struct BadgeProminence

## Overview

Badges can be used for different kinds of information, from the passive number
of items in a container to the number of required actions. The prominence of
badges in Lists can be adjusted to reflect this and be made to draw more or
less attention to themselves.

Badges will default to `standard` prominence unless specified.

The following example shows a `List` displaying a list of folders with an
informational badge with lower prominence, showing the number of items in the
folder.

## Topics

### Getting background prominence

`static let standard: BadgeProminence`

The standard level of prominence for a badge.

`static let increased: BadgeProminence`

The highest level of prominence for a badge.

`static let decreased: BadgeProminence`

The lowest level of prominence for a badge.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Displaying a badge on a list item

`func badge(Text?) -> some View`

Generates a badge for the view from a text view.

`func badge<S>(S?) -> some View`

Generates a badge for the view from a string.

`func badge(LocalizedStringKey?) -> some View`

Generates a badge for the view from a localized string key.

`func badge(Int) -> some View`

Generates a badge for the view from an integer value.

`func badgeProminence(BadgeProminence) -> some View`

Specifies the prominence of badges created by this view.

`var badgeProminence: BadgeProminence`

The prominence to apply to badges associated with this environment.

Instance Method

# swipeActions(edge:allowsFullSwipe:content:)

Adds custom swipe actions to a row in a list.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  watchOS 8.0+
visionOS 1.0+

    
    
    func swipeActions<T>(
        edge: HorizontalEdge = .trailing,
        allowsFullSwipe: Bool = true,
        @ViewBuilder content: () -> T
    ) -> some View where T : View
    

##  Parameters

`edge`

    

The edge of the view to associate the swipe actions with. The default is
`HorizontalEdge.trailing`.

`allowsFullSwipe`

    

A Boolean value that indicates whether a full swipe automatically performs the
first action. The default is `true`.

`content`

    

The content of the swipe actions.

## Discussion

Use this method to add swipe actions to a view that acts as a row in a list.
Indicate the `HorizontalEdge` where the swipe action originates, and define
individual actions with `Button` instances. For example, if you have a list of
messages, you can add an action to toggle a message as unread on a swipe from
the leading edge, and actions to delete or flag messages on a trailing edge
swipe:

Actions appear in the order you list them, starting from the swipe’s
originating edge. In the example above, the Delete action appears closest to
the screen’s trailing edge:

For labels or images that appear in swipe actions, SwiftUI automatically
applies the `fill` symbol variant, as shown above.

By default, the user can perform the first action for a given swipe direction
with a full swipe. For the example above, the user can perform both the toggle
unread and delete actions with full swipes. You can opt out of this behavior
for an edge by setting the `allowsFullSwipe` parameter to `false`. For
example, you can disable the full swipe on the leading edge:

When you set a role for a button using one of the values from the `ButtonRole`
enumeration, SwiftUI styles the button according to its role. In the example
above, the delete action appears in `red` because it has the `destructive`
role. If you want to set a different color — for example, to match the overall
theme of your app’s UI — add the `View/tint(_:)` modifier to the button:

The modifications in the code above make the toggle unread action `blue` and
the flag action `orange`:

When you add swipe actions, SwiftUI no longer synthesizes the Delete actions
that otherwise appear when using the `ForEach/onDelete(perform:)` method on a
`ForEach` instance. You become responsible for creating a Delete action, if
appropriate, among your swipe actions.

Actions accumulate for a given edge if you call the modifier multiple times on
the same list row view.

## See Also

### Configuring interaction

`func selectionDisabled(Bool) -> some View`

Adds a condition that controls whether users can select this view.

Instance Method

# selectionDisabled(_:)

Adds a condition that controls whether users can select this view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func selectionDisabled(_ isDisabled: Bool = true) -> some View
    

##  Parameters

`isDisabled`

    

A Boolean value that determines whether users can select this view.

## Discussion

Use this modifier to control the selectability of views in selectable
containers like `List` or `Table`. In the example, below, the user can’t
select the first item in the list.

You can also use this modifier to specify the selectability of views within a
`Picker`. The following example represents a flavor picker that disables
selection on flavors that are unavailable.

## See Also

### Configuring interaction

`func swipeActions<T>(edge: HorizontalEdge, allowsFullSwipe: Bool, content: ()
-> T) -> some View`

Adds custom swipe actions to a row in a list.

Instance Method

# refreshable(action:)

Marks this view as refreshable.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func refreshable(action: @escaping () async -> Void) -> some View
    

##  Parameters

`action`

    

An asynchronous handler that SwiftUI executes when the user requests a
refresh. Use this handler to initiate an update of model data displayed in the
modified view. Use `await` in front of any asynchronous calls inside the
handler.

## Return Value

A view with a new refresh action in its environment.

## Discussion

Apply this modifier to a view to set the `refresh` value in the view’s
environment to a `RefreshAction` instance that uses the specified `action` as
its handler. Views that detect the presence of the instance can change their
appearance to provide a way for the user to execute the handler.

For example, when you apply this modifier on iOS and iPadOS to a `List`, the
list enables a standard pull-to-refresh gesture that refreshes the list
contents. When the user drags the top of the scrollable area downward, the
view reveals a progress indicator and executes the specified handler. The
indicator remains visible for the duration of the refresh, which runs
asynchronously:

You can add refresh capability to your own views as well. For information on
how to do that, see `RefreshAction`.

## See Also

### Refreshing a list’s content

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

`struct RefreshAction`

An action that initiates a refresh operation.

Instance Property

# refresh

A refresh action stored in a view’s environment.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var refresh: RefreshAction? { get }

## Discussion

When this environment value contains an instance of the `RefreshAction`
structure, certain built-in views in the corresponding `Environment` begin
offering a refresh capability. They apply the instance’s handler to any
refresh operation that the user initiates. By default, the environment value
is `nil`, but you can use the `refreshable(action:)` modifier to create and
store a new refresh action that uses the handler that you specify:

On iOS and iPadOS, the `List` in the example above offers a pull to refresh
gesture because it detects the refresh action. When the user drags the list
down and releases, the list calls the action’s handler. Because SwiftUI
declares the handler as asynchronous, it can safely make long-running
asynchronous calls, like fetching network data.

### Refreshing custom views

You can also offer refresh capability in your custom views. Read the `refresh`
environment value to get the `RefreshAction` instance for a given
`Environment`. If you find a non-`nil` value, change your view’s appearance or
behavior to offer the refresh to the user, and call the instance to conduct
the refresh. You can call the refresh instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance:

Be sure to call the handler asynchronously by preceding it with `await`.
Because the call is asynchronous, you can use its lifetime to indicate
progress to the user. For example, you can reveal an indeterminate
`ProgressView` before calling the handler, and hide it when the handler
completes.

If your code isn’t already in an asynchronous context, create a `Task` for the
method to run in. If you do this, consider adding a way for the user to cancel
the task. For more information, see Concurrency in _The Swift Programming
Language_.

## See Also

### Refreshing a list’s content

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`struct RefreshAction`

An action that initiates a refresh operation.

Structure

# RefreshAction

An action that initiates a refresh operation.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct RefreshAction

## Overview

When the `refresh` environment value contains an instance of this structure,
certain built-in views in the corresponding `Environment` begin offering a
refresh capability. They apply the instance’s handler to any refresh operation
that the user initiates. By default, the environment value is `nil`, but you
can use the `refreshable(action:)` modifier to create and store a new refresh
action that uses the handler that you specify:

On iOS and iPadOS, the `List` in the example above offers a pull to refresh
gesture because it detects the refresh action. When the user drags the list
down and releases, the list calls the action’s handler. Because SwiftUI
declares the handler as asynchronous, it can safely make long-running
asynchronous calls, like fetching network data.

### Refreshing custom views

You can also offer refresh capability in your custom views. Read the `refresh`
environment value to get the `RefreshAction` instance for a given
`Environment`. If you find a non-`nil` value, change your view’s appearance or
behavior to offer the refresh to the user, and call the instance to conduct
the refresh. You can call the refresh instance directly because it defines a
`callAsFunction()` method that Swift calls when you call the instance:

Be sure to call the handler asynchronously by preceding it with `await`.
Because the call is asynchronous, you can use its lifetime to indicate
progress to the user. For example, you might reveal an indeterminate
`ProgressView` before calling the handler, and hide it when the handler
completes.

If your code isn’t already in an asynchronous context, create a `Task` for the
method to run in. If you do this, consider adding a way for the user to cancel
the task. For more information, see Concurrency in _The Swift Programming
Language_.

## Topics

### Calling the action

`func callAsFunction() async`

Initiates a refresh action.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Refreshing a list’s content

`func refreshable(action: () async -> Void) -> some View`

Marks this view as refreshable.

`var refresh: RefreshAction?`

A refresh action stored in a view’s environment.

Instance Method

# moveDisabled(_:)

Adds a condition for whether the view’s view hierarchy is movable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func moveDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Method

# deleteDisabled(_:)

Adds a condition for whether the view’s view hierarchy is deletable.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func deleteDisabled(_ isDisabled: Bool) -> some View
    

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Instance Property

# editMode

An indication of whether the user can edit the contents of a view associated
with this environment.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    var editMode: Binding<EditMode>? { get set }

## Discussion

Read this environment value to receive a optional binding to the edit mode
state. The binding contains an `EditMode` value that indicates whether edit
mode is active, and that you can use to change the mode. To learn how to read
an environment value, see `EnvironmentValues`.

Certain built-in views automatically alter their appearance and behavior in
edit mode. For example, a `List` with a `ForEach` that’s configured with the
`onDelete(perform:)` or `onMove(perform:)` modifier provides controls to
delete or move list items while in edit mode. On devices without an attached
keyboard and mouse or trackpad, people can make multiple selections in lists
only when edit mode is active.

You can also customize your own views to react to edit mode. The following
example replaces a read-only `Text` view with an editable `TextField`,
checking for edit mode by testing the wrapped value’s `isEditing` property:

You can set the edit mode through the binding, or you can rely on an
`EditButton` to do that for you, as the example above demonstrates. The button
activates edit mode when the user taps the Edit button, and disables editing
mode when the user taps Done.

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Enumeration

# EditMode

A mode that indicates whether the user can edit a view’s content.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    enum EditMode

## Overview

You receive an optional binding to the edit mode state when you read the
`editMode` environment value. The binding contains an `EditMode` value that
indicates whether edit mode is active, and that you can use to change the
mode. To learn how to read an environment value, see `EnvironmentValues`.

Certain built-in views automatically alter their appearance and behavior in
edit mode. For example, a `List` with a `ForEach` that’s configured with the
`onDelete(perform:)` or `onMove(perform:)` modifier provides controls to
delete or move list items while in edit mode. On devices without an attached
keyboard and mouse or trackpad, people can make multiple selections in lists
only when edit mode is active.

You can also customize your own views to react to edit mode. The following
example replaces a read-only `Text` view with an editable `TextField`,
checking for edit mode by testing the wrapped value’s `isEditing` property:

You can set the edit mode through the binding, or you can rely on an
`EditButton` to do that for you, as the example above demonstrates. The button
activates edit mode when the user taps it, and disables the mode when the user
taps again.

## Topics

### Getting edit modes

`case active`

The user can edit the view content.

`case inactive`

The user can’t edit the view content.

`case transient`

The view is in a temporary edit mode.

### Checking for editing mode

`var isEditing: Bool`

Indicates whether a view is being edited.

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Structure

# EditActions

A set of edit actions on a collection of data that a view can offer to a user.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct EditActions<Data>

## Topics

### Getting edit operations

`static var all: EditActions<Data>`

All the edit actions available on this collection.

Available when `Data` conforms to `MutableCollection` and
`RangeReplaceableCollection`.

`static var all: EditActions<Data>`

All the edit actions available on this collection.

Available when `Data` conforms to `MutableCollection`.

`static var all: EditActions<Data>`

All the edit actions available on this collection.

Available when `Data` conforms to `RangeReplaceableCollection`.

`static var all: EditActions<Data>`

All the edit actions available on this collection.

`static var delete: EditActions<Data>`

An edit action that allows the user to delete one or more elements of a
collection.

Available when `Data` conforms to `RangeReplaceableCollection`.

`static var move: EditActions<Data>`

An edit action that allows the user to move elements of a collection.

Available when `Data` conforms to `MutableCollection`.

### Creating an edit operation

`init(rawValue: Int)`

Creates a new set from a raw value.

`let rawValue: Int`

The raw value.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Structure

# EditableCollectionContent

An opaque wrapper view that adds editing capabilities to a row in a list.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct EditableCollectionContent<Content, Data>

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `View`

Conforms when `Content` conforms to `View`.

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct IndexedIdentifierCollection`

A collection wrapper that iterates over the indices and identifiers of a
collection together.

Structure

# IndexedIdentifierCollection

A collection wrapper that iterates over the indices and identifiers of a
collection together.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct IndexedIdentifierCollection<Base, ID> where Base : Collection, ID : Hashable

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your
behalf.

## Relationships

### Conforms To

  * `BidirectionalCollection`
  * `Collection`
  * `RandomAccessCollection`
  * `Sequence`

## See Also

### Editing a list

`func moveDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is movable.

`func deleteDisabled(Bool) -> some View`

Adds a condition for whether the view’s view hierarchy is deletable.

`var editMode: Binding<EditMode>?`

An indication of whether the user can edit the contents of a view associated
with this environment.

`enum EditMode`

A mode that indicates whether the user can edit a view’s content.

`struct EditActions`

A set of edit actions on a collection of data that a view can offer to a user.

`struct EditableCollectionContent`

An opaque wrapper view that adds editing capabilities to a row in a list.



# LayoutSubview

Instance Method

# place(at:anchor:proposal:)

Assigns a position and proposed size to the subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func place(
        at position: CGPoint,
        anchor: UnitPoint = .topLeading,
        proposal: ProposedViewSize
    )

##  Parameters

`position`

    

The place where the anchor of the subview should appear in its container view,
relative to container’s bounds.

`anchor`

    

The unit point on the subview that appears at `position`. You can use a built-
in point, like `center`, or you can create a custom `UnitPoint`.

`proposal`

    

A proposed size for the subview. In SwiftUI, views choose their own size, but
can take a size proposal from their parent view into account when doing so.

## Discussion

Call this method from your implementation of the `Layout` protocol’s
`placeSubviews(in:proposal:subviews:cache:)` method for each subview arranged
by the layout. Provide a position within the container’s bounds where the
subview should appear, and an anchor that indicates which part of the subview
appears at that point.

Include a proposed size that the subview can take into account when sizing
itself. To learn the subview’s size for a given proposal before calling this
method, you can call the `dimensions(in:)` or `sizeThatFits(_:)` method on the
subview with the same proposal. That enables you to know subview sizes before
committing to subview positions.

Important

Call this method only from within your `Layout` type’s implementation of the
`placeSubviews(in:proposal:subviews:cache:)` method.

If you call this method more than once for a subview, the last call takes
precedence. If you don’t call this method for a subview, the subview appears
at the center of its layout container and uses the layout container’s size
proposal.

Instance Method

# dimensions(in:)

Asks the subview for its dimensions and alignment guides.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func dimensions(in proposal: ProposedViewSize) -> ViewDimensions

##  Parameters

`proposal`

    

A proposed size for the subview. In SwiftUI, views choose their own size, but
can take a size proposal from their parent view into account when doing so.

## Return Value

A `ViewDimensions` instance that includes a height and width, as well as a set
of alignment guides.

## Discussion

Call this method to ask a subview of a custom `Layout` type about its size and
alignment properties. You can call it from your implementation of any of that
protocol’s methods, like `placeSubviews(in:proposal:subviews:cache:)` or
`sizeThatFits(proposal:subviews:cache:)`, to get information for your layout
calculations.

When you call this method, you propose a size using the `proposal` parameter.
The subview can choose its own size, but might take the proposal into account.
You can call this method more than once with different proposals to find out
if the view is flexible. For example, you can propose:

  * `zero` to get the subview’s minimum size.

  * `infinity` to get the subview’s maximum size.

  * `unspecified` to get the subview’s ideal size.

If you need only the view’s height and width, you can use the
`sizeThatFits(_:)` method instead.

## See Also

### Getting subview characteristics

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

`var priority: Double`

The layout priority of the subview.

Instance Method

# sizeThatFits(_:)

Asks the subview for its size.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize

##  Parameters

`proposal`

    

A proposed size for the subview. In SwiftUI, views choose their own size, but
can take a size proposal from their parent view into account when doing so.

## Return Value

The size that the subview chooses for itself, given the proposal from its
container view.

## Discussion

Use this method as a convenience to get the `width` and `height` properties of
the `ViewDimensions` instance returned by the `dimensions(in:)` method,
reported as a `CGSize` instance.

## See Also

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

`var priority: Double`

The layout priority of the subview.

Instance Property

# spacing

The subviews’s preferred spacing values.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var spacing: ViewSpacing { get }

## Discussion

This `ViewSpacing` instance indicates how much space a subview in a custom
layout prefers to have between it and the next view. It contains preferences
for all edges, and might take into account the type of both this and the
adjacent view. If your `Layout` type places subviews based on spacing
preferences, use this instance to compute a distance between this subview and
the next. See `placeSubviews(in:proposal:subviews:cache:)` for an example.

You can also merge this instance with instances from other subviews to
construct a new instance that’s suitable for the subviews’ container. See
`spacing(subviews:cache:)`.

## See Also

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var priority: Double`

The layout priority of the subview.

Instance Property

# priority

The layout priority of the subview.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    var priority: Double { get }

## Discussion

If you define a custom layout type using the `Layout` protocol, you can read
this value from subviews and use the value when deciding how to assign space
to subviews. For example, you can read all of the subview priorities into an
array before placing the subviews in a custom layout type called
`BasicVStack`:

Set the layout priority for a view that appears in your layout by applying the
`layoutPriority(_:)` view modifier. For example, you can assign two different
priorities to views that you arrange with `BasicVStack`:

## See Also

### Getting subview characteristics

`func dimensions(in: ProposedViewSize) -> ViewDimensions`

Asks the subview for its dimensions and alignment guides.

`func sizeThatFits(ProposedViewSize) -> CGSize`

Asks the subview for its size.

`var spacing: ViewSpacing`

The subviews’s preferred spacing values.

Instance Subscript

# subscript(_:)

Gets the value for the subview that’s associated with the specified key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    subscript<K>(key: K.Type) -> K.Value where K : LayoutValueKey { get }

## Overview

If you define a custom layout value using `LayoutValueKey`, you can read the
key’s associated value for a given subview in a layout container by indexing
the container’s subviews with the key type. For example, if you define a
`Flexibility` key type, you can put the associated values of all the layout’s
subviews into an array:

For more information about creating a custom layout, see `Layout`.



# LayoutValueKey

Type Property

# defaultValue

The default value of the key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var defaultValue: Self.Value { get }

**Required**

## Discussion

Implement the `defaultValue` property for a type that conforms to the
`LayoutValueKey` protocol. For example, you can create a `Flexibility` layout
value that defaults to `nil`:

The type that you declare for the `defaultValue` sets the layout key’s `Value`
associated type. The Swift compiler infers the key’s associated type in the
above example as an optional `CGFloat`.

Any view that you don’t explicitly set a value for uses the default value.
Override the default value for a view using the `layoutValue(key:value:)`
modifier.

## See Also

### Providing a default value

`associatedtype Value`

The type of the key’s value.

**Required**

Associated Type

# Value

The type of the key’s value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Value

**Required**

## Discussion

Swift typically infers this type from your implementation of the
`defaultValue` property, so you don’t have to define it explicitly.

## See Also

### Providing a default value

`static var defaultValue: Self.Value`

The default value of the key.

**Required**



# LinearKeyframe

Initializer

# init(_:duration:timingCurve:)

Creates a new keyframe using the given value and timestamp.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ to: Value,
        duration: TimeInterval,
        timingCurve: UnitCurve = .linear
    )

##  Parameters

`to`

    

The value of the keyframe.

`duration`

    

The duration of the segment defined by this keyframe.

`timingCurve`

    

A unit curve that controls the speed of interpolation.



# LinearGradient

Initializer

# init(gradient:startPoint:endPoint:)

Creates a linear gradient from a base gradient.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        gradient: Gradient,
        startPoint: UnitPoint,
        endPoint: UnitPoint
    )

## See Also

### Creating a linear gradient

`init(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint)`

Creates a linear gradient from a collection of colors.

`init(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint)`

Creates a linear gradient from a collection of color stops.

Initializer

# init(colors:startPoint:endPoint:)

Creates a linear gradient from a collection of colors.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        colors: [Color],
        startPoint: UnitPoint,
        endPoint: UnitPoint
    )

## See Also

### Creating a linear gradient

`init(gradient: Gradient, startPoint: UnitPoint, endPoint: UnitPoint)`

Creates a linear gradient from a base gradient.

`init(stops: [Gradient.Stop], startPoint: UnitPoint, endPoint: UnitPoint)`

Creates a linear gradient from a collection of color stops.

Initializer

# init(stops:startPoint:endPoint:)

Creates a linear gradient from a collection of color stops.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        stops: [Gradient.Stop],
        startPoint: UnitPoint,
        endPoint: UnitPoint
    )

## See Also

### Creating a linear gradient

`init(gradient: Gradient, startPoint: UnitPoint, endPoint: UnitPoint)`

Creates a linear gradient from a base gradient.

`init(colors: [Color], startPoint: UnitPoint, endPoint: UnitPoint)`

Creates a linear gradient from a collection of colors.



# Link

Initializer

# init(_:destination:)

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        destination: URL
    )

Available when `Label` is `Text`.

##  Parameters

`titleKey`

    

The key for the localized title that describes the purpose of this link.

`destination`

    

The URL for the link.

## Discussion

Use `Link` to create a control that your app uses to navigate to a URL that
you provide. The example below creates a link to `example.com` and uses `Visit
Example Co` as the title key to generate a link-styled view in your app:

## See Also

### Creating a link

`init<S>(S, destination: URL)`

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

Available when `Label` is `Text`.

`init(destination: URL, label: () -> Label)`

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

Initializer

# init(_:destination:)

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        destination: URL
    ) where S : StringProtocol

Available when `Label` is `Text`.

##  Parameters

`title`

    

A text string used as the title for describing the underlying `destination`
URL.

`destination`

    

The URL for the link.

## Discussion

Use `Link` to create a control that your app uses to navigate to a URL that
you provide. The example below creates a link to `example.com` and displays
the title string you provide as a link-styled view in your app:

## See Also

### Creating a link

`init(LocalizedStringKey, destination: URL)`

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

Available when `Label` is `Text`.

`init(destination: URL, label: () -> Label)`

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

Initializer

# init(destination:label:)

Creates a control, consisting of a URL and a label, used to navigate to the
given URL.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        destination: URL,
        @ViewBuilder label: () -> Label
    )

##  Parameters

`destination`

    

The URL for the link.

`label`

    

A view that describes the destination of URL.

## See Also

### Creating a link

`init(LocalizedStringKey, destination: URL)`

Creates a control, consisting of a URL and a title key, used to navigate to a
URL.

Available when `Label` is `Text`.

`init<S>(S, destination: URL)`

Creates a control, consisting of a URL and a title string, used to navigate to
a URL.

Available when `Label` is `Text`.



# LabelStyleConfiguration

Instance Property

# icon

A symbolic representation of the labeled item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var icon: LabelStyleConfiguration.Icon { get }

## See Also

### Setting the icon

`struct Icon`

A type-erased icon view of a label.

Structure

# LabelStyleConfiguration.Icon

A type-erased icon view of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct Icon

## Relationships

### Conforms To

  * `View`

## See Also

### Setting the icon

`var icon: LabelStyleConfiguration.Icon`

A symbolic representation of the labeled item.

Instance Property

# title

A description of the labeled item.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    var title: LabelStyleConfiguration.Title { get }

## See Also

### Setting the title

`struct Title`

A type-erased title view of a label.

Structure

# LabelStyleConfiguration.Title

A type-erased title view of a label.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct Title

## Relationships

### Conforms To

  * `View`

## See Also

### Setting the title

`var title: LabelStyleConfiguration.Title`

A description of the labeled item.



# LinearProgressViewStyle

Initializer

# init()

Creates a linear progress view style.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init()

Initializer

# init(tint:)

Creates a linear progress view style with a tint color.

iOS 14.0–17.4  Deprecated  iPadOS 14.0–17.4  Deprecated  macOS 11.0–14.4
Deprecated  Mac Catalyst 14.0–17.4  Deprecated  tvOS 14.0–17.4  Deprecated
watchOS 7.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(tint: Color)

Deprecated

Use the `tint(_:)` view modifier instead.



# LazyHStack

Initializer

# init(alignment:spacing:pinnedViews:content:)

Creates a lazy horizontal stack view with the given spacing, vertical
alignment, pinning behavior, and content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        alignment: VerticalAlignment = .center,
        spacing: CGFloat? = nil,
        pinnedViews: PinnedScrollableViews = .init(),
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. All child views have the
same vertical screen coordinate.

`spacing`

    

The distance between adjacent subviews, or `nil` if you want the stack to
choose a default distance for each pair of subviews.

`pinnedViews`

    

The kinds of child views that will be pinned.

`content`

    

A view builder that creates the content of this stack.



# LocalCoordinateSpace

Initializer

# init()

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# LinkShapeStyle

Initializer

# init()

Creates a new link shape style instance.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init()



# LazyVStack

Initializer

# init(alignment:spacing:pinnedViews:content:)

Creates a lazy vertical stack view with the given spacing, vertical alignment,
pinning behavior, and content.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    init(
        alignment: HorizontalAlignment = .center,
        spacing: CGFloat? = nil,
        pinnedViews: PinnedScrollableViews = .init(),
        @ViewBuilder content: () -> Content
    )

##  Parameters

`alignment`

    

The guide for aligning the subviews in this stack. All child views have the
same horizontal screen coordinate.

`spacing`

    

The distance between adjacent subviews, or `nil` if you want the stack to
choose a default distance for each pair of subviews.

`pinnedViews`

    

The kinds of child views that will be pinned.

`content`

    

A view builder that creates the content of this stack.



# ListSectionSpacing

Type Property

# default

The default spacing between sections

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static let `default`: ListSectionSpacing

## See Also

### Getting section spacing

`static let compact: ListSectionSpacing`

Compact spacing between sections

`static func custom(CGFloat) -> ListSectionSpacing`

Creates a custom spacing value.

Type Property

# compact

Compact spacing between sections

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static let compact: ListSectionSpacing

## See Also

### Getting section spacing

`static let `default`: ListSectionSpacing`

The default spacing between sections

`static func custom(CGFloat) -> ListSectionSpacing`

Creates a custom spacing value.

Type Method

# custom(_:)

Creates a custom spacing value.

iOS 17.0+  iPadOS 17.0+  Mac Catalyst 17.0+  watchOS 10.0+  visionOS 1.0+

    
    
    static func custom(_ spacing: CGFloat) -> ListSectionSpacing

##  Parameters

`spacing`

    

the amount of spacing to use.

## See Also

### Getting section spacing

`static let `default`: ListSectionSpacing`

The default spacing between sections

`static let compact: ListSectionSpacing`

Compact spacing between sections



# ListStyle

Type Property

# automatic

The list style that describes a platform’s default behavior and appearance for
a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var automatic: DefaultListStyle { get }

Available when `Self` is `DefaultListStyle`.

## See Also

### Getting built-in list styles

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# bordered

The list style that describes the behavior and appearance of a list with
standard border.

macOS 12.0+

    
    
    static var bordered: BorderedListStyle { get }

Available when `Self` is `BorderedListStyle`.

## Discussion

Bordered lists are expected to be inset from their outer containers, but do
not have inset style rows or selection.

To customize whether the rows of the list should alternate their backgrounds,
use `bordered(alternatesRowBackgrounds:)`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# carousel

The carousel list style.

watchOS 6.0+

    
    
    static var carousel: CarouselListStyle { get }

Available when `Self` is `CarouselListStyle`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# elliptical

The list style that describes the behavior and appearance of an elliptical
list.

watchOS 7.0+

    
    
    static var elliptical: EllipticalListStyle { get }

Available when `Self` is `EllipticalListStyle`.

## Discussion

On watchOS, the elliptical list style uses a transform for items rolling off
the top or bottom of the list, as if on a rounded surface that faces the user.

Apple Watch Series 3 does not support this style and will instead fall back to
using the `plain` style.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# grouped

The list style that describes the behavior and appearance of a grouped list.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    static var grouped: GroupedListStyle { get }

Available when `Self` is `GroupedListStyle`.

## Discussion

On iOS, the grouped list style displays a larger header and footer than the
`plain` style, which visually distances the members of different sections.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# inset

The list style that describes the behavior and appearance of an inset list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var inset: InsetListStyle { get }

Available when `Self` is `InsetListStyle`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# insetGrouped

The list style that describes the behavior and appearance of an inset grouped
list.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var insetGrouped: InsetGroupedListStyle { get }

Available when `Self` is `InsetGroupedListStyle`.

## Discussion

On iOS, the inset grouped list style displays a continuous background color
that extends from the section header, around both sides of list items in the
section, and down to the section footer. This visually groups the items to a
greater degree than either the `inset` or `grouped` styles do.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# plain

The list style that describes the behavior and appearance of a plain list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    static var plain: PlainListStyle { get }

Available when `Self` is `PlainListStyle`.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var sidebar: SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Available when `Self` is `SidebarListStyle`.

Type Property

# sidebar

The list style that describes the behavior and appearance of a sidebar list.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    static var sidebar: SidebarListStyle { get }

Available when `Self` is `SidebarListStyle`.

## Discussion

On macOS and iOS, the sidebar list style displays disclosure indicators in the
section headers that allow the user to collapse and expand sections.

## See Also

### Getting built-in list styles

`static var automatic: DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

Available when `Self` is `DefaultListStyle`.

`static var bordered: BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

`static var carousel: CarouselListStyle`

The carousel list style.

Available when `Self` is `CarouselListStyle`.

`static var elliptical: EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

Available when `Self` is `EllipticalListStyle`.

`static var grouped: GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

Available when `Self` is `GroupedListStyle`.

`static var inset: InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

Available when `Self` is `InsetListStyle`.

`static var insetGrouped: InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

Available when `Self` is `InsetGroupedListStyle`.

`static var plain: PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

Available when `Self` is `PlainListStyle`.

Type Method

# bordered(alternatesRowBackgrounds:)

The list style that describes the behavior and appearance of a list with
standard border.

macOS 12.0–14.4  Deprecated

    
    
    static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle

Available when `Self` is `BorderedListStyle`.

Deprecated

Use the `bordered` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

##  Parameters

`alternatesRowBackgrounds`

    

Whether the rows should alternate their backgrounds to help visually
distinguish them from each other.

## Discussion

Bordered lists are expected to be inset from their outer containers, but do
not have inset style rows or selection.

## See Also

### Deprecated styles

`static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle`

The list style that describes the behavior and appearance of an inset list
with optional alternating row backgrounds.

Available when `Self` is `InsetListStyle`.

Deprecated

Type Method

# inset(alternatesRowBackgrounds:)

The list style that describes the behavior and appearance of an inset list
with optional alternating row backgrounds.

macOS 12.0–14.4  Deprecated

    
    
    static func inset(alternatesRowBackgrounds: Bool) -> InsetListStyle

Available when `Self` is `InsetListStyle`.

Deprecated

Use the `inset` style and add the `alternatingRowBackgrounds(_:)` view
modifier instead.

##  Parameters

`alternatesRowBackgrounds`

    

Whether the rows should alternate their backgrounds to help visually
distinguish them from each other.

## See Also

### Deprecated styles

`static func bordered(alternatesRowBackgrounds: Bool) -> BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

Available when `Self` is `BorderedListStyle`.

Deprecated

Structure

# DefaultListStyle

The list style that describes a platform’s default behavior and appearance for
a list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct DefaultListStyle

## Overview

You can also use `automatic` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a default list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# BorderedListStyle

The list style that describes the behavior and appearance of a list with
standard border.

macOS 12.0+

    
    
    struct BorderedListStyle

## Overview

You can also use `bordered` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a bordered list style.

`init(alternatesRowBackgrounds: Bool)`

Creates a bordered list style with optional alternating row backgrounds.

Deprecated

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# CarouselListStyle

The carousel list style.

watchOS 6.0+

    
    
    struct CarouselListStyle

## Overview

You can also use `carousel` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a carousel list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# EllipticalListStyle

The list style that describes the behavior and appearance of an elliptical
list.

watchOS 7.0+

    
    
    struct EllipticalListStyle

## Overview

You can also use `elliptical` to construct this style.

## Topics

### Creating the list style

`init()`

Creates an elliptical list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# GroupedListStyle

The list style that describes the behavior and appearance of a grouped list.

iOS 13.0+  iPadOS 13.0+  Mac Catalyst 13.0+  tvOS 13.0+  visionOS 1.0+

    
    
    struct GroupedListStyle

## Overview

You can also use `grouped` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a grouped list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# InsetListStyle

The list style that describes the behavior and appearance of an inset list.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct InsetListStyle

## Overview

You can also use `inset` to construct this style.

## Topics

### Creating the list style

`init()`

Creates an inset list style.

`init(alternatesRowBackgrounds: Bool)`

Creates an inset list style with optional alternating row backgrounds.

Deprecated

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# InsetGroupedListStyle

The list style that describes the behavior and appearance of an inset grouped
list.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct InsetGroupedListStyle

## Overview

You can also use `insetGrouped` to construct this style.

## Topics

### Creating the list style

`init()`

Creates an inset grouped list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# PlainListStyle

The list style that describes the behavior and appearance of a plain list.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct PlainListStyle

## Overview

You can also use `plain` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a plain list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct SidebarListStyle`

The list style that describes the behavior and appearance of a sidebar list.

Structure

# SidebarListStyle

The list style that describes the behavior and appearance of a sidebar list.

iOS 14.0+  iPadOS 14.0+  macOS 10.15+  Mac Catalyst 14.0+  visionOS 1.0+

    
    
    struct SidebarListStyle

## Overview

You can also use `sidebar` to construct this style.

## Topics

### Creating the list style

`init()`

Creates a sidebar list style.

## Relationships

### Conforms To

  * `ListStyle`

## See Also

### Supporting types

`struct DefaultListStyle`

The list style that describes a platform’s default behavior and appearance for
a list.

`struct BorderedListStyle`

The list style that describes the behavior and appearance of a list with
standard border.

`struct CarouselListStyle`

The carousel list style.

`struct EllipticalListStyle`

The list style that describes the behavior and appearance of an elliptical
list.

`struct GroupedListStyle`

The list style that describes the behavior and appearance of a grouped list.

`struct InsetListStyle`

The list style that describes the behavior and appearance of an inset list.

`struct InsetGroupedListStyle`

The list style that describes the behavior and appearance of an inset grouped
list.

`struct PlainListStyle`

The list style that describes the behavior and appearance of a plain list.



# LabeledContent

Initializer

# init(_:content:)

Creates a labeled view that generates its label from a localized string key.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`titleKey`

    

The key for the view’s localized title, that describes the purpose of the
view.

`content`

    

The value content being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating labeled content

`init<S>(S, content: () -> Content)`

Creates a labeled view that generates its label from a string.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(_:content:)

Creates a labeled view that generates its label from a string.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` conforms to `View`.

##  Parameters

`title`

    

A string that describes the purpose of the view.

`content`

    

The value content being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating labeled content

`init(LocalizedStringKey, content: () -> Content)`

Creates a labeled view that generates its label from a localized string key.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init(content: () -> Content, label: () -> Label)`

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

Available when `Label` conforms to `View` and `Content` conforms to `View`.

Initializer

# init(content:label:)

Creates a standard labeled element, with a view that conveys the value of the
element and a label.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder label: () -> Label
    )

Available when `Label` conforms to `View` and `Content` conforms to `View`.

##  Parameters

`content`

    

The view that conveys the value of the resulting labeled element.

`label`

    

The label that describes the purpose of the result.

## See Also

### Creating labeled content

`init(LocalizedStringKey, content: () -> Content)`

Creates a labeled view that generates its label from a localized string key.

Available when `Label` is `Text` and `Content` conforms to `View`.

`init<S>(S, content: () -> Content)`

Creates a labeled view that generates its label from a string.

Available when `Label` is `Text` and `Content` conforms to `View`.

Initializer

# init(_:value:)

Creates a labeled informational view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S>(
        _ titleKey: LocalizedStringKey,
        value: S
    ) where S : StringProtocol

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`titleKey`

    

The key for the view’s localized title, that describes the purpose of the
view.

`value`

    

The value being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

In some contexts, this text will be selectable by default.

## See Also

### Creating informational views

`init<S1, S2>(S1, value: S2)`

Creates a labeled informational view.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:value:)

Creates a labeled informational view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S1, S2>(
        _ title: S1,
        value: S2
    ) where S1 : StringProtocol, S2 : StringProtocol

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the view.

`value`

    

The value being labeled.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating informational views

`init<S>(LocalizedStringKey, value: S)`

Creates a labeled informational view.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:value:format:)

Creates a labeled informational view from a formatted value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<F>(
        _ titleKey: LocalizedStringKey,
        value: F.FormatInput,
        format: F
    ) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`titleKey`

    

The key for the view’s localized title, that describes the purpose of the
view.

`value`

    

The value being labeled.

`format`

    

A format style of type `F` to convert the underlying value of type
`F.FormatInput` to a string representation.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the
localized key similar to `init(_:tableName:bundle:comment:)`. See `Text` for
more information about localizing strings.

## See Also

### Creating formatted labeled content

`init<S, F>(S, value: F.FormatInput, format: F)`

Creates a labeled informational view from a formatted value.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:value:format:)

Creates a labeled informational view from a formatted value.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init<S, F>(
        _ title: S,
        value: F.FormatInput,
        format: F
    ) where S : StringProtocol, F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == String

Available when `Label` is `Text` and `Content` is `Text`.

##  Parameters

`title`

    

A string that describes the purpose of the view.

`value`

    

The value being labeled.

`format`

    

A format style of type `F` to convert the underlying value of type
`F.FormatInput` to a string representation.

## Discussion

This initializer creates a `Text` label on your behalf, and treats the title
similar to `init(_:)`. See `Text` for more information about localizing
strings.

## See Also

### Creating formatted labeled content

`init<F>(LocalizedStringKey, value: F.FormatInput, format: F)`

Creates a labeled informational view from a formatted value.

Available when `Label` is `Text` and `Content` is `Text`.

Initializer

# init(_:)

Creates labeled content based on a labeled content style configuration.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    init(_ configuration: LabeledContentStyleConfiguration)

Available when `Label` is `LabeledContentStyleConfiguration.Label` and
`Content` is `LabeledContentStyleConfiguration.Content`.

##  Parameters

`configuration`

    

The properties of the labeled content

## Discussion

You can use this initializer within the `makeBody(configuration:)` method of a
`LabeledContentStyle` to create a labeled content instance. This is useful for
custom styles that only modify the current style, as opposed to implementing a
brand new style.

For example, the following style adds a red border around the labeled content,
but otherwise preserves the current style:



# LayoutDirection

Case

# LayoutDirection.leftToRight

A left-to-right layout direction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case leftToRight

## See Also

### Getting layout directions

`case rightToLeft`

A right-to-left layout direction.

Case

# LayoutDirection.rightToLeft

A right-to-left layout direction.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case rightToLeft

## See Also

### Getting layout directions

`case leftToRight`

A left-to-right layout direction.

Initializer

# init(_:)

Create a direction from its UITraitEnvironmentLayoutDirection equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiLayoutDirection: UITraitEnvironmentLayoutDirection)



# LegibilityWeight

Case

# LegibilityWeight.regular

Use regular font weight (no Accessibility Bold).

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case regular

## See Also

### Getting weights

`case bold`

Use heavier font weight (force Accessibility Bold).

Case

# LegibilityWeight.bold

Use heavier font weight (force Accessibility Bold).

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    case bold

## See Also

### Getting weights

`case regular`

Use regular font weight (no Accessibility Bold).

Initializer

# init(_:)

Creates a legibility weight from its UILegibilityWeight equivalent.

iOS 14.0+  iPadOS 14.0+  Mac Catalyst 14.0+  tvOS 14.0+  visionOS 1.0+

    
    
    init?(_ uiLegibilityWeight: UILegibilityWeight)



# LinearCapacityGaugeStyle

Initializer

# init()

Creates a linear capacity gauge style.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  watchOS 9.0+
visionOS 1.0+

    
    
    init()



# Layout

Instance Method

# sizeThatFits(proposal:subviews:cache:)

Returns the size of the composite view, given a proposed size and the view’s
subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func sizeThatFits(
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> CGSize

**Required**

##  Parameters

`proposal`

    

A size proposal for the container. The container’s parent view that calls this
method might call the method more than once with different proposals to learn
more about the container’s flexibility before deciding which proposal to use
for placement.

`subviews`

    

A collection of proxies that represent the views that the container arranges.
You can use the proxies in the collection to get information about the
subviews as you determine how much space the container needs to display them.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

A size that indicates how much space the container needs to arrange its
subviews.

## Discussion

Implement this method to tell your custom layout container’s parent view how
much space the container needs for a set of subviews, given a size proposal.
The parent might call this method more than once during a layout pass with
different proposed sizes to test the flexibility of the container, using
proposals like:

  * The `zero` proposal; respond with the layout’s minimum size.

  * The `infinity` proposal; respond with the layout’s maximum size.

  * The `unspecified` proposal; respond with the layout’s ideal size.

The parent might also choose to test flexibility in one dimension at a time.
For example, a horizontal stack might propose a fixed height and an infinite
width, and then the same height with a zero width.

The following example calculates the size for a basic vertical stack that
places views in a column, with no spacing between the views:

The implementation asks each subview for its ideal size by calling the
`sizeThatFits(_:)` method with an `unspecified` proposed size. It then reduces
these values into a single size that represents the maximum subview width and
the sum of subview heights. Because this example isn’t flexible, it ignores
its size proposal input and always returns the same value for a given set of
subviews.

SwiftUI views choose their own size, so the layout engine always uses a value
that you return from this method as the actual size of the composite view.
That size factors into the construction of the `bounds` input to the
`placeSubviews(in:proposal:subviews:cache:)` method.

## See Also

### Sizing the container and placing subviews

`func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews:
Self.Subviews, cache: inout Self.Cache)`

Assigns positions to each of the layout’s subviews.

**Required**

` typealias Subviews`

A collection of proxies for the subviews of a layout view.

Instance Method

# placeSubviews(in:proposal:subviews:cache:)

Assigns positions to each of the layout’s subviews.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func placeSubviews(
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    )

**Required**

##  Parameters

`bounds`

    

The region that the container view’s parent allocates to the container view,
specified in the parent’s coordinate space. Place all the container’s subviews
within the region. The size of this region matches a size that your container
previously returned from a call to the
`sizeThatFits(proposal:subviews:cache:)` method.

`proposal`

    

The size proposal from which the container generated the size that the parent
used to create the `bounds` parameter. The parent might propose more than one
size before calling the placement method, but it always uses one of the
proposals and the corresponding returned size when placing the container.

`subviews`

    

A collection of proxies that represent the views that the container arranges.
Use the proxies in the collection to get information about the subviews and to
tell the subviews where to appear.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Discussion

SwiftUI calls your implementation of this method to tell your custom layout
container to place its subviews. From this method, call the
`place(at:anchor:proposal:)` method on each element in `subviews` to tell the
subviews where to appear in the user interface.

For example, you can create a basic vertical stack that places views in a
column, with views horizontally aligned on their leading edge:

The example creates a placement point that starts at the origin of the
specified `bounds` input and uses that to place the first subview. It then
moves the point in the y dimension by the subview’s height, which it reads
using the `dimensions(in:)` method. This prepares the point for the next
iteration of the loop. All subview operations use an `unspecified` size
proposal to indicate that subviews should use and report their ideal size.

A more complex layout container might add space between subviews according to
their `spacing` preferences, or a fixed space based on input configuration.
For example, you can extend the basic vertical stack’s placement method to
calculate the preferred distances between adjacent subviews and store the
results in an array:

The spacing’s `distance(to:along:)` method considers the preferences of
adjacent views on the edge where they meet. It returns the smallest distance
that satisfies both views’ preferences for the given edge. For example, if one
view prefers at least `2` points on its bottom edge, and the next view prefers
at least `8` points on its top edge, the distance method returns `8`, because
that’s the smallest value that satisfies both preferences.

Update the placement calculations to use the spacing values:

Be sure that you use computations during placement that are consistent with
those in your implementation of other protocol methods for a given set of
inputs. For example, if you add spacing during placement, make sure your
implementation of `sizeThatFits(proposal:subviews:cache:)` accounts for the
extra space. Similarly, if the sizing method returns different values for
different size proposals, make sure the placement method responds to its
`proposal` input in the same way.

## See Also

### Sizing the container and placing subviews

`func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache:
inout Self.Cache) -> CGSize`

Returns the size of the composite view, given a proposed size and the view’s
subviews.

**Required**

` typealias Subviews`

A collection of proxies for the subviews of a layout view.

Type Alias

# Layout.Subviews

A collection of proxies for the subviews of a layout view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    typealias Subviews = LayoutSubviews

## Discussion

This collection doesn’t store views. Instead it stores instances of
`LayoutSubview`, each of which acts as a proxy for one of the views arranged
by the layout. Use the proxies to get information about the views, and to tell
the views where to appear.

For more information about the behavior of the underlying collection type, see
`LayoutSubviews`.

## See Also

### Sizing the container and placing subviews

`func sizeThatFits(proposal: ProposedViewSize, subviews: Self.Subviews, cache:
inout Self.Cache) -> CGSize`

Returns the size of the composite view, given a proposed size and the view’s
subviews.

**Required**

` func placeSubviews(in: CGRect, proposal: ProposedViewSize, subviews:
Self.Subviews, cache: inout Self.Cache)`

Assigns positions to each of the layout’s subviews.

**Required**

Instance Method

# explicitAlignment(of:in:proposal:subviews:cache:)

Returns the position of the specified horizontal alignment guide along the x
axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func explicitAlignment(
        of guide: HorizontalAlignment,
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> CGFloat?

**Required** Default implementations provided.

##  Parameters

`guide`

    

The `HorizontalAlignment` guide that the method calculates the position of.

`bounds`

    

The region that the container view’s parent allocates to the container view,
specified in the parent’s coordinate space.

`proposal`

    

A proposed size for the container.

`subviews`

    

A collection of proxy instances that represent the views arranged by the
container. You can use the proxies in the collection to get information about
the subviews as you determine where to place the guide.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

The guide’s position relative to the `bounds`. Return `nil` to indicate that
the guide doesn’t have an explicit value.

## Discussion

Implement this method to return a value for the specified alignment guide of a
custom layout container. The value you return affects the placement of the
container as a whole, but it doesn’t affect how the container arranges
subviews relative to one another.

You can use this method to put an alignment guide in a nonstandard position.
For example, you can indent the container’s leading edge alignment guide by 10
points:

The above example returns `nil` for other guides to indicate that they don’t
have an explicit value. A guide without an explicit value behaves as it would
for any other view. If you don’t implement the method, the protocol’s default
implementation merges the subviews’ guides.

## Default Implementations

### Layout Implementations

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the vertical alignment guides of all subviews.

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the horizontal alignment guides of all subviews.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

Instance Method

# explicitAlignment(of:in:proposal:subviews:cache:)

Returns the position of the specified vertical alignment guide along the y
axis.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func explicitAlignment(
        of guide: VerticalAlignment,
        in bounds: CGRect,
        proposal: ProposedViewSize,
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> CGFloat?

**Required** Default implementations provided.

##  Parameters

`guide`

    

The `VerticalAlignment` guide that the method calculates the position of.

`bounds`

    

The region that the container view’s parent allocates to the container view,
specified in the parent’s coordinate space.

`proposal`

    

A proposed size for the container.

`subviews`

    

A collection of proxy instances that represent the views arranged by the
container. You can use the proxies in the collection to get information about
the subviews as you determine where to place the guide.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

The guide’s position relative to the `bounds`. Return `nil` to indicate that
the guide doesn’t have an explicit value.

## Discussion

Implement this method to return a value for the specified alignment guide of a
custom layout container. The value you return affects the placement of the
container as a whole, but it doesn’t affect how the container arranges
subviews relative to one another.

You can use this method to put an alignment guide in a nonstandard position.
For example, you can raise the container’s bottom edge alignment guide by 10
points:

The above example returns `nil` for other guides to indicate that they don’t
have an explicit value. A guide without an explicit value behaves as it would
for any other view. If you don’t implement the method, the protocol’s default
implementation merges the subviews’ guides.

## Default Implementations

### Layout Implementations

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the vertical alignment guides of all subviews.

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the result of merging the horizontal alignment guides of all subviews.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

Instance Method

# spacing(subviews:cache:)

Returns the preferred spacing values of the composite view.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func spacing(
        subviews: Self.Subviews,
        cache: inout Self.Cache
    ) -> ViewSpacing

**Required** Default implementation provided.

##  Parameters

`subviews`

    

A collection of proxy instances that represent the views that the container
arranges. You can use the proxies in the collection to get information about
the subviews as you determine how much spacing the container prefers around
it.

`cache`

    

Optional storage for calculated data that you can share among the methods of
your custom layout container. See `makeCache(subviews:)` for details.

## Return Value

A `ViewSpacing` instance that describes the preferred spacing around the
container view.

## Discussion

Implement this method to provide custom spacing preferences for a layout
container. The value you return affects the spacing around the container, but
it doesn’t affect how the container arranges subviews relative to one another
inside the container.

Create a custom `ViewSpacing` instance for your container by initializing one
with default values, and then merging that with spacing instances of certain
subviews. For example, if you define a basic vertical stack that places
subviews in a column, you could use the spacing preferences of the subview
edges that make contact with the container’s edges:

In the above example, the first and last subviews contribute to the spacing
above and below the container, respectively, while all subviews affect the
spacing on the leading and trailing edges.

If you don’t implement this method, the protocol provides a default
implementation, namely `spacing(subviews:cache:)`, that merges the spacing
preferences across all subviews on all edges.

## Default Implementations

### Layout Implementations

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the union of all subview spacing.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`static var layoutProperties: LayoutProperties`

Properties of a layout container.

**Required** Default implementation provided.

Type Property

# layoutProperties

Properties of a layout container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    static var layoutProperties: LayoutProperties { get }

**Required** Default implementation provided.

## Discussion

Implement this property in a type that conforms to the `Layout` protocol to
characterize your custom layout container. For example, you can indicate that
your layout has a vertical `stackOrientation`:

If you don’t implement this property in your custom layout, the protocol
provides a default implementation, namely `layoutProperties`, that returns a
`LayoutProperties` instance with default values.

## Default Implementations

### Layout Implementations

`static var layoutProperties: LayoutProperties`

The default property values for a layout.

## See Also

### Reporting layout container characteristics

`func explicitAlignment(of: HorizontalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified horizontal alignment guide along the x
axis.

**Required** Default implementations provided.

`func explicitAlignment(of: VerticalAlignment, in: CGRect, proposal:
ProposedViewSize, subviews: Self.Subviews, cache: inout Self.Cache) ->
CGFloat?`

Returns the position of the specified vertical alignment guide along the y
axis.

**Required** Default implementations provided.

`func spacing(subviews: Self.Subviews, cache: inout Self.Cache) ->
ViewSpacing`

Returns the preferred spacing values of the composite view.

**Required** Default implementation provided.

Instance Method

# makeCache(subviews:)

Creates and initializes a cache for a layout instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func makeCache(subviews: Self.Subviews) -> Self.Cache

**Required** Default implementation provided.

##  Parameters

`subviews`

    

A collection of proxy instances that represent the views that the container
arranges. You can use the proxies in the collection to get information about
the subviews as you calculate values to store in the cache.

## Return Value

Storage for calculated data that you share among the methods of your custom
layout container.

## Discussion

You can optionally use a cache to preserve calculated values across calls to a
layout container’s methods. Many layout types don’t need a cache, because
SwiftUI automatically reuses both the results of calls into the layout and the
values that the layout reads from its subviews. Rely on the protocol’s default
implementation of this method if you don’t need a cache.

However you might find a cache useful when:

  * The layout container repeats complex, intermediate calculations across calls like `sizeThatFits(proposal:subviews:cache:)`, `placeSubviews(in:proposal:subviews:cache:)`, and `explicitAlignment(of:in:proposal:subviews:cache:)`. You might be able to improve performance by calculating values once and storing them in a cache.

  * The layout container reads many `LayoutValueKey` values from subviews. It might be more efficient to do that once and store the results in the cache, rather than rereading the subviews’ values before each layout call.

  * You want to maintain working storage, like temporary Swift arrays, across calls into the layout, to minimize the number of allocation events.

Only implement a cache if profiling shows that it improves performance.

### Initialize a cache

Implement the `makeCache(subviews:)` method to create a cache. You can add
computed values to the cache right away, using information from the `subviews`
input parameter, or you can do that later. The methods of the `Layout`
protocol that can access the cache take the cache as an in-out parameter,
which enables you to modify the cache anywhere that you can read it.

You can use any storage type that makes sense for your layout algorithm, but
be sure that you only store data that you derive from the layout and its
subviews (lazily, if possible). For this to work correctly, SwiftUI needs to
be able to call this method to recreate the cache without changing the layout
result.

When you return a cache from this method, you implicitly define a type for
your cache. Be sure to either make the type of the `cache` parameters on your
other `Layout` protocol methods match, or use a type alias to define the
`Cache` associated type.

### Update the cache

If the layout container or any of its subviews change, SwiftUI calls the
`updateCache(_:subviews:)` method so you can modify or invalidate the contents
of the cache. The default implementation of that method calls the
`makeCache(subviews:)` method to recreate the cache, but you can provide your
own implementation of the update method to take an incremental approach, if
appropriate.

## Default Implementations

### Layout Implementations

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Returns the empty value when your layout doesn’t require a cache.

Available when `Cache` is `()`.

## See Also

### Managing a cache

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Updates the layout’s cache when something changes.

**Required** Default implementation provided.

`associatedtype Cache = Void`

Cached values associated with the layout instance.

**Required**

Instance Method

# updateCache(_:subviews:)

Updates the layout’s cache when something changes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func updateCache(
        _ cache: inout Self.Cache,
        subviews: Self.Subviews
    )

**Required** Default implementation provided.

##  Parameters

`cache`

    

Storage for calculated data that you share among the methods of your custom
layout container.

`subviews`

    

A collection of proxy instances that represent the views arranged by the
container. You can use the proxies in the collection to get information about
the subviews as you calculate values to store in the cache.

## Discussion

If your custom layout container creates a cache by implementing the
`makeCache(subviews:)` method, SwiftUI calls the update method when your
layout or its subviews change, giving you an opportunity to modify or
invalidate the contents of the cache. The method’s default implementation
recreates the cache by calling the `makeCache(subviews:)` method, but you can
provide your own implementation to take an incremental approach, if
appropriate.

## Default Implementations

### Layout Implementations

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Reinitializes a cache to a new value.

## See Also

### Managing a cache

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Creates and initializes a cache for a layout instance.

**Required** Default implementation provided.

`associatedtype Cache = Void`

Cached values associated with the layout instance.

**Required**

Associated Type

# Cache

Cached values associated with the layout instance.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    associatedtype Cache = Void

**Required**

## Discussion

If you create a cache for your custom layout, you can use a type alias to
define this type as your data storage type. Alternatively, you can refer to
the data storage type directly in all the places where you work with the
cache.

See `makeCache(subviews:)` for more information.

## See Also

### Managing a cache

`func makeCache(subviews: Self.Subviews) -> Self.Cache`

Creates and initializes a cache for a layout instance.

**Required** Default implementation provided.

`func updateCache(inout Self.Cache, subviews: Self.Subviews)`

Updates the layout’s cache when something changes.

**Required** Default implementation provided.

Instance Method

# callAsFunction(_:)

Combines the specified views into a single composite view using the layout
algorithms of the custom layout container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func callAsFunction<V>(@ViewBuilder _ content: () -> V) -> some View where V : View
    

##  Parameters

`content`

    

A `ViewBuilder` that contains the views to lay out.

## Return Value

A composite view that combines all the input views.

## Discussion

Don’t call this method directly. SwiftUI calls it when you instantiate a
custom layout that conforms to the `Layout` protocol:

For information about how Swift uses the `callAsFunction()` method to simplify
call site syntax, see Methods with Special Names in _The Swift Programming
Language_.



# Layout Implementations

Structure

# GridLayout.Cache

A stateful grid layout algorithm.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    struct Cache



# Layout fundamentals

Article

# Picking container views for your content

Build flexible user interfaces by using stacks, grids, lists, and forms.

## Overview

SwiftUI provides a range of container views that group and repeat views. Use
some containers purely for structure and layout, like stack views, lazy stack
views, and grid views. Use others, like lists and forms, to also adopt system-
standard visuals and interactivity.

Choosing the most appropriate container views for each part of your app’s user
interface is an important skill to learn; it helps you with everything from
positioning two views next to each other, to creating complex layouts with
hundreds of elements.

### Group collections of views

Stack views are the most primitive layout container available in SwiftUI. Use
stacks to group collections of views into horizontal or vertical lines, or to
stack them on top of one another.

Use `HStack` to lay out views in a horizontal line, `VStack` to position views
in a vertical line, and `ZStack` to layer views on top of one another. Then,
combine stack views to compose more complex layouts. These three kinds of
stacks, along with their alignment and spacing properties, view modifiers, and
`Spacer` views combine to allow extensive layout flexibility.

You often use stack views as building blocks inside other container views. For
example, a `List` typically contains stack views, with which you lay out views
inside each row.

For more information on using stack views to lay out views, see Building
layouts with stack views.

### Repeat views or groups of views

You can also use `HStack`, `VStack`, `LazyHStack`, and `LazyVStack` to repeat
views or groups of views. Place a stack view inside a `ScrollView` so your
content can expand beyond the bounds of its container. Users can
simultaneously scroll horizontally, vertically, or in both directions.

Stack views and lazy stacks have similar functionality, and they may feel
interchangeable, but they each have strengths in different situations. Stack
views load their child views all at once, making layout fast and reliable,
because the system knows the size and shape of every subview as it loads them.
Lazy stacks trade some degree of layout correctness for performance, because
the system only calculates the geometry for subviews as they become visible.

When choosing the type of stack view to use, always start with a standard
stack view and only switch to a lazy stack if profiling your code shows a
worthwhile performance improvement. For more information on lazy stack views
and how to measure your app’s view loading performance, see Creating
performant scrollable stacks.

### Position views in a two-dimensional layout

To lay out views horizontally and vertically at the same time, use a
`LazyVGrid` or `LazyHGrid`. Grids are a good container choice to lay out
content that naturally displays in square containers, like an image gallery.
Grids are also a good choice to scale user interface layouts up for display on
larger devices. For example, a directory of contact information might suit a
list or vertical stack on an iPhone, but might fit more naturally in a grid
layout when scaled up to a larger device like the iPad or Mac.

Like stack views, SwiftUI grid views don’t inherently include a scrolling
viewport; place them inside a `ScrollView` if the content might be larger than
the available space.

### Display and interact with collections of data

`List` views in SwiftUI are conceptually similar to the combination of a
`LazyVStack` and `ScrollView`, but by default will include platform-
appropriate visual styling around and between their contained items. For
example, when running on iOS, the default configuration of a `List` adds
separator lines between rows, and draws disclosure indicators for items which
have navigation, and where the list is contained in a `NavigationView`.

`List` views also support platform-appropriate interactivity for common tasks
such as inserting, reordering, and removing items. For example, adding the
`onDelete(perform:)` modifier to a `ForEach` inside a `List` will enable
system-standard swipe-to-delete interactivity.

Like `LazyHStack` and `LazyVStack`, rows inside a SwiftUI `List` also load
lazily, and there is no non-lazy equivalent. Lists inherently scroll when
necessary, and you don’t need to wrap them in a `ScrollView`.

### Group views and controls for data entry

Use `Form` to build data-entry interfaces, settings, or preference screens
that use system-standard controls.

Like all SwiftUI views, forms display their content in a platform-appropriate
way. Be aware that the layout of controls inside a `Form` may differ
significantly based on the platform. For example, a `Picker` control in a
`Form` on iOS adds navigation, showing the picker’s choices on a separate
screen, while the same `Picker` on macOS displays a pop-up button or set of
radio buttons.

Article

# Building layouts with stack views

Compose complex layouts from primitive container views.

## Overview

Individually, `HStack`, `VStack`, and `ZStack` are simple views. `HStack`
positions views in a horizontal line, `VStack` positions them in a vertical
line, and `ZStack` overlays views on top of one another.

When you initialize them with default parameters, stack views center align
their content and insert a small amount of spacing between each contained
view. But, when you combine and customize stacks with view modifiers,
`Spacer`, and `Divider` views, you can create highly flexible and complex
layouts.

### Plan your layout hierarchy

Think about a layout in terms of how you might create it using the various
types of stack views as you start to translate your design into code. Break
down complex designs into smaller, simpler pieces you can build with stack
views.

For example, you might build this profile view using three stack views:

A `ZStack` contains an `Image` view that displays a profile picture with a
semi-transparent `HStack` overlaid on top. The `HStack` contains a `VStack`
with a pair of `Text` views inside it, and a `Spacer` view pushes the `VStack`
to the leading side.

To create this stack view:

### Position views with alignment and spacer views

Align any contained views inside a stack view by using a combination of the
`alignment` property, `Spacer`, and `Divider` views.

In the previous example layout, the `VStack` that contains the two `Text`
views uses the `leading` alignment:

The `alignment` property doesn’t position the `VStack` inside its container;
instead, it positions the views inside the `VStack`.

The `alignment` property of a `VStack` only applies to the horizontal
alignment of the contained controls using `HorizontalAlignment`. Similarly,
the `alignment` property for an `HStack` only controls the vertical alignment
using `VerticalAlignment`. Finally, you can align views inside a `ZStack`
along both axes with `Alignment`.

Use `Spacer` views to align views along the primary axis of an `HStack` or
`VStack`. Spacers expand to fill any available space and push content apart
from other views or the edges of the stack.

`Divider` views also add space in between a stack’s subviews, but only insert
enough space to draw a line across the stack’s minor axis. They don’t expand
to fill available space.

### Create adaptive layouts instead of explicit layouts

Wherever possible, define structure and hierarchy rather than explicitly
positioning view frames. Instead of using explicit heights and widths for
views, let them expand to fill available space. Adaptive layouts that you
build adapt more easily to different device sizes and platforms.

It is possible to create this article’s example layout with two stack views
rather than three, by manipulating the `Text` view frames explicitly. While
the output might look the same, the code to implement it is more brittle, and
might not scale as well across devices of different size classes.

You may need to make adjustments to a layout that uses explicit adjustments by
using view modifiers such as `frame(width:height:alignment:)` or
`position(x:y:)`, but only consider this when you can’t achieve your desired
layout in an adaptive, flexible way. For more information on making fine
adjustments to view layout, see Making fine adjustments to a view’s position.

### Add depth in alternative ways

In some situations it may make sense to add depth to your layout by using the
`overlay(_:alignment:)` and `background(_:alignment:)` view modifiers instead
of a `ZStack`. The background view modifier places another view behind the
view you’re modifying, and overlay places a view on top of it.

Choose between a stack-based approach and the view modifier approach based on
how you want to determine the size of the final layout. If your layout has one
dominant view that defines the size of the layout, use the
`overlay(_:alignment:)` or `background(_:alignment:)` view modifier on that
view. If you want the final view size to come from an aggregation of all the
contained views, use a `ZStack`.

For example, this code overlays a `ProfileDetail` view on top of the `Image`
view:

## See Also

### Statically arranging views in one dimension

`struct HStack`

A view that arranges its subviews in a horizontal line.

`struct VStack`

A view that arranges its subviews in a vertical line.

Structure

# HStack

A view that arranges its subviews in a horizontal line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct HStack<Content> where Content : View

## Overview

Unlike `LazyHStack`, which only renders the views when your app needs to
display them onscreen, an `HStack` renders the views all at once, regardless
of whether they are on- or offscreen. Use the regular `HStack` when you have a
small number of subviews or don’t want the delayed rendering behavior of the
“lazy” version.

The following example shows a simple horizontal stack of five text views:

Note

If you need a horizontal stack that conforms to the `Layout` protocol, like
when you want to create a conditional layout using `AnyLayout`, use
`HStackLayout` instead.

## Topics

### Creating a stack

`init(alignment: VerticalAlignment, spacing: CGFloat?, content: () ->
Content)`

Creates a horizontal stack with the given spacing and vertical alignment.

## Relationships

### Conforms To

  * `View`

## See Also

### Statically arranging views in one dimension

Building layouts with stack views

Compose complex layouts from primitive container views.

`struct VStack`

A view that arranges its subviews in a vertical line.

Structure

# VStack

A view that arranges its subviews in a vertical line.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct VStack<Content> where Content : View

## Overview

Unlike `LazyVStack`, which only renders the views when your app needs to
display them, a `VStack` renders the views all at once, regardless of whether
they are on- or offscreen. Use the regular `VStack` when you have a small
number of subviews or don’t want the delayed rendering behavior of the “lazy”
version.

The following example shows a simple vertical stack of 10 text views:

Note

If you need a vertical stack that conforms to the `Layout` protocol, like when
you want to create a conditional layout using `AnyLayout`, use `VStackLayout`
instead.

## Topics

### Creating a stack

`init(alignment: HorizontalAlignment, spacing: CGFloat?, content: () ->
Content)`

Creates an instance with the given spacing and horizontal alignment.

## Relationships

### Conforms To

  * `View`

## See Also

### Statically arranging views in one dimension

Building layouts with stack views

Compose complex layouts from primitive container views.

`struct HStack`

A view that arranges its subviews in a horizontal line.

Article

# Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

## Overview

`LazyHStack` and `LazyVStack` views are both able to display groups of views
organized into logical sections, arranging their children in lines that grow
horizontally and vertically, respectively. These stacks are “lazy” in that the
stack views don’t create items until they need to be rendered onscreen. Like
stack views, lazy stacks don’t include any inherent support for scrolling, and
you should wrap lazy stack views in `ScrollView` containers.

To group content or data inside a lazy stack view, use `Section` instances as
containers for collections of grouped views. `Section` views don’t have any
visual representation themselves but can contain header and footer views that
can either scroll with the stack’s content or that you can pin to the top or
bottom of the `ScrollView`.

Note

Use `Section` views to get platform-appropriate grouping inside stack views or
lazy stacks, lazy grids, `List`, `CommandMenu`, `Form`, and several other
container types.

The code samples in this article build a user interface for visualizing shades
of primary colors. Each section in the stack represents a primary color,
containing five subviews, each showing a different variation of the color.

### Prepare your data

As with views contained within a stack, each `Section` must be uniquely
identifiable when iterated by `ForEach`. In this example, `ColorData`
instances represent the sections, and `ShadeData` instances represent the
shades of each color inside a section. Both `ColorData` and `ShadeData`
conform to the `Identifiable` protocol.

### Display sections with headers and footers

The `ColorSelectionView` below sets up an array containing `ColorData`
instances for each primary color. The `LazyVStack` iterates over the array of
color data to create sections, then iterates over the `variations` to create
views from the shades.

Group data with `Section` views and pass in a header or footer view with the
`header` and `footer` properties. This example implements a
`SectionHeaderView` as a header view, containing a semi-transparent stack view
and the name of the section’s color in a `Text` label.

For more information on using `ForEach` to repeat views inside a stack, see
Creating performant scrollable stacks.

### Keep important information visible

By default, section header and footer views will scroll in sync with section
content. If you want header and footer views to always remain visible,
regardless of whether the top or bottom of the section is visible, then
specify a set of `PinnedScrollableViews` for the `pinnedViews` property of the
lazy stack view.

In `LazyVStack` containers, headers attach to the top and footers to the
bottom. In `LazyHStack` containers, headers attach to the leading edge and
footers to the trailing edge.

With this change, section headers are pinned to the top of the view as the
user begins to scroll.

## See Also

### Dynamically arranging views in one dimension

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Article

# Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

## Overview

Your apps often need to display more data within a container view than there
is space for on a device’s screen. Horizontal and vertical stacks are a good
solution for repeating views or groups of views, but they don’t have a built-
in mechanism for scrolling. You can add scrolling by wrapping stacks inside a
`ScrollView`, and switch to lazy stacks as performance issues arise.

### Display groups of views in a scrollable container

Implementing repeating views or groups of views can be as simple as wrapping
them in an `HStack` or `VStack` inside a `ScrollView`.

If the `ProfileView` in the example code above has an intrinsic content size
of 200 x 200 points, the maximum width of 500 points that the
`frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)`
view modifier applies to the `ScrollView` causes the stack to scroll inside
it.

For an introduction to using stacks to group views together, see Building
layouts with stack views.

### Repeat views for your data

Use `ForEach` to repeat views for the data in your app. From a list of profile
data in a `profiles` array, use `ForEach` to create one `ProfileView` per
element in the array inside an `HStack`.

Note

When you use `ForEach`, each element you iterate over must be uniquely
identifiable. Either conform elements to the `Identifiable` protocol, or pass
a key path to a unique identifier as the `id` parameter of
`init(_:id:content:)`.

### Consider lazy stacks for large numbers of views

The three standard stack views, `HStack`, `VStack`, and `ZStack`, all load
their contained view hierarchy when they display, and loading large numbers of
views all at once can result in slow runtime performance.

In the above example, `ProfileView` is a compound view that consists of nested
stack views, text labels, and an image view. Loading a large number of
profiles all at once causes a noticeable slowdown.

As the number of views inside a stack grows, consider using a `LazyHStack` and
`LazyVStack` instead of `HStack` and `VStack`. Lazy stacks load and render
their subviews on-demand, providing significant performance gains when loading
large numbers of subviews.

Stack views and lazy stacks have similar functionality, and they may feel
interchangeable, but they each have strengths in different situations. Stack
views load their child views all at once, making layout fast and reliable,
because the system knows the size and shape of every subview as it loads them.
Lazy stacks trade some degree of layout correctness for performance, because
the system only calculates the geometry for subviews as they become visible.

When choosing the type of stack view to use, always start with a standard
stack view and only switch to a lazy stack if profiling your code shows a
worthwhile performance improvement.

### Profile to find performance problems

When considering which type of stack to use, use the Instruments tool to
profile your application to identify the areas of your user interface code
where large numbers of views are loading inside a stack.

To profile SwiftUI view loading, open the Instruments tool by selecting
Profile from the Xcode Product menu and choosing the SwiftUI profiling
template. This template loads four instruments: View Body, View Properties,
Core Animation Commits, and Time Profiler. The combination of these
instruments provides a good starting point to find opportunities to speed up
your app.

Note

Never profile your code using the iOS simulator. Always use real devices for
performance testing.

When profiling the above code, the View Body instrument shows that 1,000
`ProfileView` instances load into memory at the same time as the `HStack`. You
can also see the same number of `Image` views load as the system loads each
profile.

In this case, the solution is to replace the `HStack` with a `LazyHStack` as
the following code shows:

Running another trace shows a drastic reduction in the number of initially
loaded views as only four `ProfileView` instances start as visible. You can
also see a corresponding decrease in the Total Duration column.

For more information about using the Instruments tool, see
doc://com.apple.documentation/documentation/metrickit/improving_your_app_s_performance.

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Structure

# LazyHStack

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyHStack<Content> where Content : View

## Overview

The stack is “lazy,” in that the stack view doesn’t create items until it
needs to render them onscreen.

In the following example, a `ScrollView` contains a `LazyHStack` that consists
of a horizontal row of text views. The stack aligns to the top of the scroll
view and uses 10-point spacing between each text view.

## Topics

### Creating a lazy-loading horizontal stack

`init(alignment: VerticalAlignment, spacing: CGFloat?, pinnedViews:
PinnedScrollableViews, content: () -> Content)`

Creates a lazy horizontal stack view with the given spacing, vertical
alignment, pinning behavior, and content.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Structure

# LazyVStack

A view that arranges its children in a line that grows vertically, creating
items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyVStack<Content> where Content : View

## Overview

The stack is “lazy,” in that the stack view doesn’t create items until it
needs to render them onscreen.

In the following example, a `ScrollView` contains a `LazyVStack` that consists
of a vertical row of text views. The stack aligns to the leading edge of the
scroll view, and uses default spacing between the text views.

## Topics

### Creating a lazy-loading vertical stack

`init(alignment: HorizontalAlignment, spacing: CGFloat?, pinnedViews:
PinnedScrollableViews, content: () -> Content)`

Creates a lazy vertical stack view with the given spacing, vertical alignment,
pinning behavior, and content.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct PinnedScrollableViews`

A set of view types that may be pinned to the bounds of a scroll view.

Structure

# PinnedScrollableViews

A set of view types that may be pinned to the bounds of a scroll view.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct PinnedScrollableViews

## Topics

### Getting scrollable view types

`static let sectionHeaders: PinnedScrollableViews`

The header view of each `Section` will be pinned.

`static let sectionFooters: PinnedScrollableViews`

The footer view of each `Section` will be pinned.

## Relationships

### Conforms To

  * `Equatable`
  * `ExpressibleByArrayLiteral`
  * `OptionSet`
  * `RawRepresentable`
  * `Sendable`
  * `SetAlgebra`

## See Also

### Dynamically arranging views in one dimension

Grouping data with lazy stack views

Split content into logical sections inside lazy stack views.

Creating performant scrollable stacks

Display large numbers of repeated views efficiently with scroll views, stack
views, and lazy stacks.

`struct LazyHStack`

A view that arranges its children in a line that grows horizontally, creating
items only as needed.

`struct LazyVStack`

A view that arranges its children in a line that grows vertically, creating
items only as needed.

Structure

# Grid

A container view that arranges other views in a two dimensional layout.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct Grid<Content> where Content : View

## Overview

Create a two dimensional layout by initializing a `Grid` with a collection of
`GridRow` structures. The first view in each grid row appears in the grid’s
first column, the second view in the second column, and so on. The following
example creates a grid with two rows and two columns:

A grid and its rows behave something like a collection of `HStack` instances
wrapped in a `VStack`. However, the grid handles row and column creation as a
single operation, which applies alignment and spacing to cells, rather than
first to rows and then to a column of unrelated rows. The grid produced by the
example above demonstrates this:

Note

If you need a grid that conforms to the `Layout` protocol, like when you want
to create a conditional layout using `AnyLayout`, use `GridLayout` instead.

### Multicolumn cells

If you provide a view rather than a `GridRow` as an element in the grid’s
content, the grid uses the view to create a row that spans all of the grid’s
columns. For example, you can add a `Divider` between the rows of the previous
example:

Because a divider takes as much horizontal space as its parent offers, the
entire grid widens to fill the width offered by its parent view.

To prevent a flexible view from taking more space on a given axis than the
other cells in a row or column require, add the `gridCellUnsizedAxes(_:)` view
modifier to the view:

This restores the grid to the width that the text and images require:

To make a cell span a specific number of columns rather than the whole grid,
use the `gridCellColumns(_:)` modifier on a view that’s contained inside a
`GridRow`.

### Column count

The grid’s column count grows to handle the row with the largest number of
columns. If you create rows with different numbers of columns, the grid adds
empty cells to the trailing edge of rows that have fewer columns. The example
below creates three rows with different column counts:

The resulting grid has as many columns as the widest row, adding empty cells
to rows that don’t specify enough views:

The grid sets the width of all the cells in a column to match the needs of
column’s widest cell. In the example above, the width of the first column
depends on the width of the widest `Text` view that the column contains. The
other columns, which contain flexible `Color` views, share the remaining
horizontal space offered by the grid’s parent view equally.

Similarly, the tallest cell in a row sets the height of the entire row. The
cells in the first column of the grid above need only the height required for
each string, but the `Color` cells expand to equally share the total height
available to the grid. As a result, the color cells determine the row heights.

### Cell spacing and alignment

You can control the spacing between cells in both the horizontal and vertical
dimensions and set a default alignment for the content in all the grid cells
when you initialize the grid using the
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer.
Consider a modified version of the previous example:

This configuration causes all of the cells to use `bottom` alignment — which
only affects the text cells because the colors fill their cells completely —
and it reduces the spacing between cells:

You can override the alignment of specific cells or groups of cells. For
example, you can change the horizontal alignment of the cells in a column by
adding the `gridColumnAlignment(_:)` modifier, or the vertical alignment of
the cells in a row by configuring the row’s `init(alignment:content:)`
initializer. You can also align a single cell with the `gridCellAnchor(_:)`
modifier.

### Performance considerations

A grid can size its rows and columns correctly because it renders all of its
child views immediately. If your app exhibits poor performance when it first
displays a large grid that appears inside a `ScrollView`, consider switching
to a `LazyVGrid` or `LazyHGrid` instead.

Lazy grids render their cells when SwiftUI needs to display them, rather than
all at once. This reduces the initial cost of displaying a large scrollable
grid that’s never fully visible, but also reduces the grid’s ability to
optimally lay out cells. Switch to a lazy grid only if profiling your code
shows a worthwhile performance improvement.

## Topics

### Creating a grid

`init(alignment: Alignment, horizontalSpacing: CGFloat?, verticalSpacing:
CGFloat?, content: () -> Content)`

Creates a grid with the specified spacing, alignment, and child views.

## Relationships

### Conforms To

  * `View`

Conforms when `Content` conforms to `View`.

## See Also

### Statically arranging views in two dimensions

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Structure

# GridRow

A horizontal row in a two dimensional grid container.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct GridRow<Content> where Content : View

## Overview

Use one or more `GridRow` instances to define the rows of a `Grid` container.
The child views inside the row define successive grid cells. You can add rows
to the grid explicitly, or use the `ForEach` structure to generate multiple
rows. Similarly, you can add cells to the row explicitly or you can use
`ForEach` to generate multiple cells inside the row. The following example
mixes these strategies:

The grid in the example above has an explicit first row and three generated
rows. Similarly, each row has an explicit first cell and three generated
cells:

To create an empty cell, use something invisible, like the `clear` color that
appears in the first column of the first row in the example above. However, if
you use a flexible view like a `Color` or a `Spacer`, you might also need to
add the `gridCellUnsizedAxes(_:)` modifier to prevent the view from taking up
more space than the other cells in the row or column need.

Important

You can’t use `EmptyView` to create a blank cell because that resolves to the
absence of a view and doesn’t generate a cell.

By default, the cells in the row use the `Alignment` that you define when you
initialize the `Grid`. However, you can override the vertical alignment for
the cells in a row by providing a `VerticalAlignment` value to the row’s
`init(alignment:content:)` initializer.

If you apply a view modifier to a row, the row applies the modifier to all of
the cells, similar to how a `Group` behaves. For example, if you apply the
`border(_:width:)` modifier to a row, SwiftUI draws a border on each cell in
the row rather than around the row.

## Topics

### Creating a grid row

`init(alignment: VerticalAlignment?, content: () -> Content)`

Creates a horizontal row of child views in a grid.

## Relationships

### Conforms To

  * `View`

Conforms when `Content` conforms to `View`.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellColumns(_:)

Tells a view that acts as a cell in a grid to span the specified number of
columns.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellColumns(_ count: Int) -> some View
    

##  Parameters

`count`

    

The number of columns that the view should consume when placed in a grid row.

## Return Value

A view that occupies the specified number of columns in a grid row.

## Discussion

By default, each view that you put into the content closure of a `GridRow`
corresponds to exactly one column of the grid. Apply the `gridCellColumns(_:)`
modifier to a view that you want to span more than one column, as in the
following example of a typical macOS configuration view:

The `Toggle` in the example above spans the column that contains the font
names and the column that contains the buttons:

Important

When you tell a cell to span multiple columns, the grid changes the merged
cell to use anchor alignment, rather than the usual alignment guides. For
information about the behavior of anchor alignment, see `gridCellAnchor(_:)`.

As a convenience you can cause a view to span all of the `Grid` columns by
placing the view directly in the content closure of the `Grid`, outside of a
`GridRow`, and omitting the modifier. To do the opposite and include more than
one view in a cell, group the views using an appropriate layout container,
like an `HStack`, so that they act as a single view.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellAnchor(_:)

Specifies a custom alignment anchor for a view that acts as a grid cell.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellAnchor(_ anchor: UnitPoint) -> some View
    

##  Parameters

`anchor`

    

The unit point that defines how to align the view within the bounds of its
grid cell.

## Return Value

A view that uses the specified anchor point to align its content.

## Discussion

Grids, like stacks and other layout containers, perform most alignment
operations using alignment guides. The grid moves the contents of each cell in
a row in the y direction until the specified `VerticalAlignment` guide of each
view in the row aligns with the same guide of all the other views in the row.
Similarly, the grid aligns the `HorizontalAlignment` guides of views in a
column by adjusting views in the x direction. See the guide types for more
information about typical SwiftUI alignment operations.

When you use the `gridCellAnchor(_:)` modifier on a view in a grid, the grid
changes to an anchor-based alignment strategy for the associated cell. With
anchor alignment, the grid projects a `UnitPoint` that you specify onto both
the view and the cell, and aligns the two projections. For example, consider
the following grid:

The grid creates red reference squares in the first row and column to
establish row and column sizes. Without the anchor modifier, the blue marker
in the remaining cell would appear at the center of its cell, because of the
grid’s default `center` alignment. With the anchor modifier shown in the code
above, the grid aligns the one quarter point of the marker with the one
quarter point of its cell in the x direction, as measured from the origin at
the top left of the cell. The grid also aligns the three quarters point of the
marker with the three quarters point of the cell in the y direction:

`UnitPoint` defines many convenience points that correspond to the typical
alignment guides, which you can use as well. For example, you can use
`topTrailing` to align the top and trailing edges of a view in a cell with the
top and trailing edges of the cell:

Applying the anchor-based alignment strategy to a single cell doesn’t affect
the alignment strategy that the grid uses on other cells.

### Anchor alignment for merged cells

If you use the `gridCellColumns(_:)` modifier to cause a cell to span more
than one column, or if you place a view in a grid outside of a row so that the
view spans the entire grid, the grid automatically converts its vertical and
horizontal alignment guides to the unit point equivalent for the merged cell,
and uses an anchor-based approach for that cell. For example, the following
grid places the marker at the center of the merged cell by converting the
grid’s default `center` alignment guide to a `center` anchor for the blue
marker in the merged cell:

The grid makes this conversion in part to avoid ambiguity. Each column has its
own horizontal guide, and it isn’t clear which of these a cell that spans
multiple columns should align with. Further, in the example above, neither of
the center alignment guides for the second or third column would provide the
expected behavior, which is to center the marker in the merged cell. Anchor
alignment provides this behavior:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridCellUnsizedAxes(_:)

Asks grid layouts not to offer the view extra size in the specified axes.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridCellUnsizedAxes(_ axes: Axis.Set) -> some View
    

##  Parameters

`axes`

    

The dimensions in which the grid shouldn’t offer the view a share of any
available space. This prevents a flexible view like a `Spacer`, `Divider`, or
`Color` from defining the size of a row or column.

## Return Value

A view that doesn’t ask an enclosing grid for extra size in one or more axes.

## Discussion

Use this modifier to prevent a flexible view from taking more space on the
specified axes than the other cells in a row or column require. For example,
consider the following `Grid` that places a `Divider` between two rows of
content:

The text and images all have ideal widths for their content. However, because
a divider takes as much space as its parent offers, the grid fills the width
of the display, expanding all the other cells to match:

You can prevent the grid from giving the divider more width than the other
cells require by adding the modifier with the `Axis.horizontal` parameter:

This restores the grid to the width that it would have without the divider:

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridColumnAlignment(HorizontalAlignment) -> some View`

Overrides the default horizontal alignment of the grid column that the view
appears in.

Instance Method

# gridColumnAlignment(_:)

Overrides the default horizontal alignment of the grid column that the view
appears in.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    func gridColumnAlignment(_ guide: HorizontalAlignment) -> some View
    

##  Parameters

`guide`

    

The `HorizontalAlignment` guide to use for the grid column that the view
appears in.

## Return Value

A view that uses the specified horizontal alignment, and that causes all cells
in the same column of a grid to use the same alignment.

## Discussion

You set a default alignment for the cells in a grid in both vertical and
horizontal dimensions when you create the grid with the
`init(alignment:horizontalSpacing:verticalSpacing:content:)` initializer.
However, you can use the `gridColumnAlignment(_:)` modifier to override the
horizontal alignment of a column within the grid. The following example sets a
grid’s alignment to `leadingFirstTextBaseline`, and then sets the first column
to use `trailing` alignment:

This creates the layout of a typical macOS configuration view, with the
trailing edge of the first column flush with the leading edge of the second
column:

Add the modifier to only one cell in a column. The grid automatically aligns
all cells in that column the same way. You get undefined behavior if you apply
different alignments to different cells in the same column.

To override row alignment, see `init(alignment:content:)`. To override
alignment for a single cell, see `gridCellAnchor(_:)`.

## See Also

### Statically arranging views in two dimensions

`struct Grid`

A container view that arranges other views in a two dimensional layout.

`struct GridRow`

A horizontal row in a two dimensional grid container.

`func gridCellColumns(Int) -> some View`

Tells a view that acts as a cell in a grid to span the specified number of
columns.

`func gridCellAnchor(UnitPoint) -> some View`

Specifies a custom alignment anchor for a view that acts as a grid cell.

`func gridCellUnsizedAxes(Axis.Set) -> some View`

Asks grid layouts not to offer the view extra size in the specified axes.

Structure

# LazyHGrid

A container view that arranges its child views in a grid that grows
horizontally, creating items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyHGrid<Content> where Content : View

## Overview

Use a lazy horizontal grid when you want to display a large, horizontally
scrollable collection of views arranged in a two dimensional layout. The first
view that you provide to the grid’s `content` closure appears in the top row
of the column that’s on the grid’s leading edge. Additional views occupy
successive cells in the grid, filling the first column from top to bottom,
then the second column, and so on. The number of columns can grow unbounded,
but you specify the number of rows by providing a corresponding number of
`GridItem` instances to the grid’s initializer.

The grid in the following example defines two rows and uses a `ForEach`
structure to repeatedly generate a pair of `Text` views for the rows in each
column:

For each column in the grid, the top row shows a Unicode code point from the
“Smileys” group, and the bottom shows its corresponding emoji:

You can achieve a similar layout using a `Grid` container. Unlike a lazy grid,
which creates child views only when SwiftUI needs to display them, a regular
grid creates all of its child views right away. This enables the grid to
provide better support for cell spacing and alignment. Only use a lazy grid if
profiling your app shows that a `Grid` view performs poorly because it tries
to load too many views at once.

## Topics

### Creating a horizontal grid

`init(rows: [GridItem], alignment: VerticalAlignment, spacing: CGFloat?,
pinnedViews: PinnedScrollableViews, content: () -> Content)`

Creates a grid that grows horizontally.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in two dimensions

`struct LazyVGrid`

A container view that arranges its child views in a grid that grows
vertically, creating items only as needed.

`struct GridItem`

A description of a row or a column in a lazy grid.

Structure

# LazyVGrid

A container view that arranges its child views in a grid that grows
vertically, creating items only as needed.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct LazyVGrid<Content> where Content : View

## Overview

Use a lazy vertical grid when you want to display a large, vertically
scrollable collection of views arranged in a two dimensional layout. The first
view that you provide to the grid’s `content` closure appears in the top row
of the column that’s on the grid’s leading edge. Additional views occupy
successive cells in the grid, filling the first row from leading to trailing
edges, then the second row, and so on. The number of rows can grow unbounded,
but you specify the number of columns by providing a corresponding number of
`GridItem` instances to the grid’s initializer.

The grid in the following example defines two columns and uses a `ForEach`
structure to repeatedly generate a pair of `Text` views for the columns in
each row:

For each row in the grid, the first column shows a Unicode code point from the
“Smileys” group, and the second shows its corresponding emoji:

You can achieve a similar layout using a `Grid` container. Unlike a lazy grid,
which creates child views only when SwiftUI needs to display them, a regular
grid creates all of its child views right away. This enables the grid to
provide better support for cell spacing and alignment. Only use a lazy grid if
profiling your app shows that a `Grid` view performs poorly because it tries
to load too many views at once.

## Topics

### Creating a vertical grid

`init(columns: [GridItem], alignment: HorizontalAlignment, spacing: CGFloat?,
pinnedViews: PinnedScrollableViews, content: () -> Content)`

Creates a grid that grows vertically.

## Relationships

### Conforms To

  * `View`

## See Also

### Dynamically arranging views in two dimensions

`struct LazyHGrid`

A container view that arranges its child views in a grid that grows
horizontally, creating items only as needed.

`struct GridItem`

A description of a row or a column in a lazy grid.

Structure

# GridItem

A description of a row or a column in a lazy grid.

iOS 14.0+  iPadOS 14.0+  macOS 11.0+  Mac Catalyst 14.0+  tvOS 14.0+  watchOS
7.0+  visionOS 1.0+

    
    
    struct GridItem

## Overview

Use an array of `GridItem` instances to configure the layout of items in a
lazy grid. Each grid item in the array specifies layout properties like size
and spacing for the rows of a `LazyHGrid` or the columns of a `LazyVGrid`. The
following example defines four rows for a horizontal grid, each with different
characteristics:

A lazy horizontal grid sets the width of each column based on the widest cell
in the column. It can do this because it has access to all of the views in a
given column at once. In the example above, the `Color` views always have the
same fixed width, resulting in a uniform column width across the whole grid.

However, a lazy horizontal grid doesn’t generally have access to all the views
in a row, because it generates new cells as people scroll through information
in your app. Instead, it relies on a grid item for information about each row.
The example above indicates a different fixed height for each row, and sets a
different amount of spacing to appear after each row:

## Topics

### Creating a grid item

`init(GridItem.Size, spacing: CGFloat?, alignment: Alignment?)`

Creates a grid item with the specified size, spacing, and alignment.

### Inspecting grid item properties

`var alignment: Alignment?`

The alignment to use when placing each view.

`var spacing: CGFloat?`

The spacing to the next item.

`var size: GridItem.Size`

The size of the item, which is the width of a column item or the height of a
row item.

`enum Size`

The size in the minor axis of one or more rows or columns in a grid layout.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Dynamically arranging views in two dimensions

`struct LazyHGrid`

A container view that arranges its child views in a grid that grows
horizontally, creating items only as needed.

`struct LazyVGrid`

A container view that arranges its child views in a grid that grows
vertically, creating items only as needed.

Article

# Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

## Overview

You can add a view as a background with the `background(_:alignment:)` view
modifier. To add a background under multiple views, or to have a background
larger than an existing view, you can layer the views by placing them within a
`ZStack`, and place the view you want to be in the background at the bottom of
the view stack. You can specify that a background view should ignore the safe
area insets to extend the background to some or all edges.

### Add a background

If your design calls for a background, you can use the
`background(_:alignment:)` modifier to add it underneath an existing view. The
following example adds a gradient to the vertical stack using the
`background(_:alignment:)` view modifier:

The `background(_:alignment:)` view modifier constrains the size of the
background view to be the same size as the view to which it’s attached:

### Expand the background underneath your view

To create a background that’s larger than the vertical stack, use a different
technique. You could add `Spacer` views above and below the content in the
`VStack` to expand it, but that would also expand the size of the stack,
possibly changing it’s layout. To add in a larger background without changing
the size of the stack, nest the views within a `ZStack` to layer the `VStack`
over the background view:

View sizes within a depth stack are independent, unlike when using the
background view modifier. The view from `Gradient` expands to fill the space
available to the stack, but avoids the safe area insets by default:

For more information on usings stacks to combine views, see Building layouts
with stack views.

### Extend the background into the safe areas

By default, SwiftUI sizes and positions views to avoid system defined safe
areas to ensure that system content or the edges of the device won’t obstruct
your views. If your design calls for the background to extend to the screen
edges, use the `ignoresSafeArea(_:edges:)` modifier to override the default.

The background gradient fills the display area of the device and ignores the
safe area insets.

### Adjust views when displaying the keyboard

You can ignore the keyboard’s safe area by adding the
`ignoresSafeArea(_:edges:)` modifier. When you activate the keyboard, the
content of the vertical stack remains fixed, ignoring the space used by the
keyboard:

To get the contents of the vertical stack to respect the safe areas and adjust
to the keyboard, move the modifier to only apply to the background view.

To accommodate the keyboard, SwiftUI resizes and positions your view. Because
the background view has the `ignoresSafeArea(_:edges:)` modifier, it remains
unchanged.

## See Also

### Layering views

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Structure

# ZStack

A view that overlays its subviews, aligning them in both axes.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct ZStack<Content> where Content : View

## Overview

The `ZStack` assigns each successive subview a higher z-axis value than the
one before it, meaning later subviews appear “on top” of earlier ones.

The following example creates a `ZStack` of 100 x 100 point `Rectangle` views
filled with one of six colors, offsetting each successive subview by 10 points
so they don’t completely overlap:

The `ZStack` uses an `Alignment` to set the x- and y-axis coordinates of each
subview, defaulting to a `center` alignment. In the following example, the
`ZStack` uses a `bottomLeading` alignment to lay out two subviews, a red 100 x
50 point rectangle below, and a blue 50 x 100 point rectangle on top. Because
of the alignment value, both rectangles share a bottom-left corner with the
`ZStack` (in locales where left is the leading side).

Note

If you need a version of this stack that conforms to the `Layout` protocol,
like when you want to create a conditional layout using `AnyLayout`, use
`ZStackLayout` instead.

## Topics

### Creating a stack

`init(alignment: Alignment, content: () -> Content)`

Creates an instance with the given alignment.

## Relationships

### Conforms To

  * `View`

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# zIndex(_:)

Controls the display order of overlapping views.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    func zIndex(_ value: Double) -> some View
    

##  Parameters

`value`

    

A relative front-to-back ordering for this view; the default is `0`.

## Discussion

Use `zIndex(_:)` when you want to control the front-to-back ordering of views.

In this example there are two overlapping rotated rectangles. The frontmost is
represented by the larger index value.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(alignment:content:)

Layers the views that you specify behind this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw behind this view,
stacked in a cascading order from bottom to top. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a background.

## Discussion

Use this modifier to place one or more views behind another view. For example,
you can place a collection of stars beind a `Text` view:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places behind the text:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can layer a vertical bar
behind a circle, with both of those behind a horizontal bar:

Both the background modifier and the implicit `ZStack` composed from the
background content — the circle and the vertical bar — use a default `center`
alignment. The vertical bar appears centered behind the circle, and both
appear as a composite view centered behind the horizontal bar:

If you specify an alignment for the background, it applies to the implicit
stack rather than to the individual views in the closure. You can see this if
you add the `leading` alignment:

The vertical bar and the circle move as a unit to align the stack with the
leading edge of the horizontal bar, while the vertical bar remains centered on
the circle:

To control the placement of individual items inside the `content` closure,
either use a different background modifier for each item, as the earlier
example of stars under text demonstrates, or add an explicit `ZStack` inside
the content closure with its own alignment:

The stack alignment ensures that the circle’s leading edge aligns with the
vertical bar’s, while the background modifier aligns the composite view with
the horizontal bar:

You can achieve layering without a background modifier by putting both the
modified view and the background content into a `ZStack`. This produces a
simpler view hierarchy, but it changes the layout priority that SwiftUI
applies to the views. Use the background modifier when you want the modified
view to dominate the layout.

If you want to specify a `ShapeStyle` like a `HierarchicalShapeStyle` or a
`Material` as the background, use `background(_:ignoresSafeAreaEdges:)`
instead. To specify a `Shape` or `InsettableShape`, use
`background(_:in:fillStyle:)` or `background(_:in:fillStyle:)`, respectively.
To configure the background of a presentation, like a sheet, use
`presentationBackground(alignment:content:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:ignoresSafeAreaEdges:)

Sets the view’s background to a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI draws behind
the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the specified style drawn behind it.

## Discussion

Use this modifier to place a type that conforms to the `ShapeStyle` protocol —
like a `Color`, `Material`, or `HierarchicalShapeStyle` — behind a view. For
example, you can add the `regularMaterial` behind a `Label`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
background fills the entirety of the label’s frame, which includes the
padding:

SwiftUI limits the background style’s extent to the modified view’s container-
relative shape. You can see this effect if you constrain the `FlagLabel` view
with a `containerShape(_:)` modifier:

The background takes on the specified container shape:

By default, the background ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(ignoresSafeAreaEdges:)

Sets the view’s background to the default background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background(ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View
    

##  Parameters

`edges`

    

The set of edges for which to ignore safe area insets when adding the
background. The default value is `all`. Specify an empty set to respect safe
area insets on all edges.

## Return Value

A view with the `background` shape style drawn behind it.

## Discussion

This modifier behaves like `background(_:ignoresSafeAreaEdges:)`, except that
it always uses the `background` shape style. For example, you can add a
background to a `Label`:

Without the background modifier, the teal color behind the label shows through
the label. With the modifier, the label’s text and icon appear backed by a
region filled with a color that’s appropriate for light or dark appearance:

If you want to specify a `View` or a stack of views as the background, use
`background(alignment:content:)` instead. To specify a `Shape` or
`InsettableShape`, use `background(_:in:fillStyle:)` or
`background(_:in:fillStyle:)`, respectively. To configure the background of a
presentation, like a sheet, use `presentationBackground(_:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to an insettable shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : InsettableShape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `InsettableShape`
protocol — like a `Rectangle`, `Circle`, or `Capsule` — behind a view. Specify
the `ShapeStyle` that’s used to fill the shape. For example, you can place a
`RoundedRectangle` behind a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to an insettable shape filled with the default
background style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : InsettableShape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `InsettableShape` that SwiftUI draws
behind the view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified insettable shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified insettable
shape. For example, you can use a `RoundedRectangle` as a background on a
`Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(_:in:fillStyle:)

Sets the view’s background to a shape filled with a style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol behind
a view. Specify the `ShapeStyle` that’s used to fill the shape. For example,
you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

The `teal` color fills the shape:

This modifier and `background(_:in:fillStyle:)` are convenience methods for
placing a single shape behind a view. To create a background with other `View`
types — or with a stack of views — use `background(alignment:content:)`
instead. To add a `ShapeStyle` as a background, use
`background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# background(in:fillStyle:)

Sets the view’s background to a shape filled with the default background
style.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func background<S>(
        in shape: S,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : Shape
    

##  Parameters

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws behind the
view using the `background` shape style.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn behind it.

## Discussion

This modifier behaves like `background(_:in:fillStyle:)`, except that it
always uses the `background` shape style to fill the specified shape. For
example, you can create a `Path` that outlines a trapezoid:

Then you can use that shape as a background for a `Label`:

Without the background modifier, the fill color shows through the label. With
the modifier, the label’s text and icon appear backed by a shape filled with a
color that’s appropriate for light or dark appearance:

To create a background with other `View` types — or with a stack of views —
use `background(alignment:content:)` instead. To add a `ShapeStyle` as a
background, use `background(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(alignment:content:)

Layers the views that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<V>(
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the foreground views. The default is `center`.

`content`

    

A `ViewBuilder` that you use to declare the views to draw in front of this
view, stacked in the order that you list them. The last view that you list
appears at the front of the stack.

## Return Value

A view that uses the specified content as a foreground.

## Discussion

Use this modifier to place one or more views in front of another view. For
example, you can place a group of stars on a `RoundedRectangle`:

The example above assumes that you’ve defined a `Star` view with a
parameterized color:

By setting different `alignment` values for each modifier, you make the stars
appear in different places on the rectangle:

If you specify more than one view in the `content` closure, the modifier
collects all of the views in the closure into an implicit `ZStack`, taking
them in order from back to front. For example, you can place a star and a
`Circle` on a field of `blue`:

Both the overlay modifier and the implicit `ZStack` composed from the overlay
content — the circle and the star — use a default `center` alignment. The star
appears centered on the circle, and both appear as a composite view centered
in front of the square:

If you specify an alignment for the overlay, it applies to the implicit stack
rather than to the individual views in the closure. You can see this if you
add the `bottom` alignment:

The circle and the star move down as a unit to align the stack’s bottom edge
with the bottom edge of the square, while the star remains centered on the
circle:

To control the placement of individual items inside the `content` closure,
either use a different overlay modifier for each item, as the earlier example
of stars in the corners of a rectangle demonstrates, or add an explicit
`ZStack` inside the content closure with its own alignment:

The stack alignment ensures that the star’s bottom edge aligns with the
circle’s, while the overlay aligns the composite view with the square:

You can achieve layering without an overlay modifier by putting both the
modified view and the overlay content into a `ZStack`. This can produce a
simpler view hierarchy, but changes the layout priority that SwiftUI applies
to the views. Use the overlay modifier when you want the modified view to
dominate the layout.

If you want to specify a `ShapeStyle` like a `Color` or a `Material` as the
overlay, use `overlay(_:ignoresSafeAreaEdges:)` instead. To specify a `Shape`,
use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:ignoresSafeAreaEdges:)

Layers the specified style in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S>(
        _ style: S,
        ignoresSafeAreaEdges edges: Edge.Set = .all
    ) -> some View where S : ShapeStyle
    

##  Parameters

`style`

    

An instance of a type that conforms to `ShapeStyle` that SwiftUI layers in
front of the modified view.

`edges`

    

The set of edges for which to ignore safe area insets when adding the overlay.
The default value is `all`. Specify an empty set to respect safe area insets
on all edges.

## Return Value

A view with the specified style drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `ShapeStyle` protocol,
like a `Color`, `Material`, or `HierarchicalShapeStyle`, in front of a view.
For example, you can overlay the `ultraThinMaterial` over a `Circle`:

SwiftUI anchors the style to the view’s bounds. For the example above, the
overlay fills the entirety of the circle’s frame (which happens to be wider
than the circle is tall):

SwiftUI also limits the style’s extent to the view’s container-relative shape.
You can see this effect if you constrain the `CoveredCircle` view with a
`containerShape(_:)` modifier:

The overlay takes on the specified container shape:

By default, the overlay ignores safe area insets on all edges, but you can
provide a specific set of edges to ignore, or an empty set to respect safe
area insets on all edges:

If you want to specify a `View` or a stack of views as the overlay rather than
a style, use `overlay(alignment:content:)` instead. If you want to specify a
`Shape`, use `overlay(_:in:fillStyle:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# overlay(_:in:fillStyle:)

Layers a shape that you specify in front of this view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    func overlay<S, T>(
        _ style: S,
        in shape: T,
        fillStyle: FillStyle = FillStyle()
    ) -> some View where S : ShapeStyle, T : Shape
    

##  Parameters

`style`

    

A `ShapeStyle` that SwiftUI uses to the fill the shape that you specify.

`shape`

    

An instance of a type that conforms to `Shape` that SwiftUI draws in front of
the view.

`fillStyle`

    

The `FillStyle` to use when drawing the shape. The default style uses the
nonzero winding number rule and antialiasing.

## Return Value

A view with the specified shape drawn in front of it.

## Discussion

Use this modifier to layer a type that conforms to the `Shape` protocol — like
a `Rectangle`, `Circle`, or `Capsule` — in front of a view. Specify a
`ShapeStyle` that’s used to fill the shape. For example, you can overlay the
outline of one rectangle in front of another:

The example above uses the `inset(by:)` method to slightly reduce the size of
the overlaid rectangle, and the `stroke(lineWidth:)` method to fill only the
shape’s outline. This creates an inset border:

This modifier is a convenience method for layering a shape over a view. To
handle the more general case of overlaying a `View` — or a stack of views —
with control over the position, use `overlay(alignment:content:)` instead. To
cover a view with a `ShapeStyle`, use `overlay(_:ignoresSafeAreaEdges:)`.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Property

# backgroundMaterial

The material underneath the current view.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    var backgroundMaterial: Material? { get set }

## Discussion

This value is `nil` if the current background isn’t one of the standard
materials. If you set a material, the standard content styles enable their
vibrant rendering modes.

You set this value by calling one of the background modifiers that takes a
`ShapeStyle`, like `background(_:ignoresSafeAreaEdges:)` or
`background(_:in:fillStyle:)`, and passing in a `Material`. You can also set
the value manually, using `nil` to disable vibrant rendering, or a `Material`
instance to enable the vibrancy style associated with the specified material.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# containerBackground(_:for:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<S>(
        _ style: S,
        for container: ContainerBackgroundPlacement
    ) -> some View where S : ShapeStyle
    

## Discussion

The following example uses a `LinearGradient` as a background:

The `.containerBackground(_:for:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

  * Parameters

    * style: The shape style to use as the container background.

    * container: The container that will use the background.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Instance Method

# containerBackground(for:alignment:content:)

Sets the container background of the enclosing container using a view.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    func containerBackground<V>(
        for container: ContainerBackgroundPlacement,
        alignment: Alignment = .center,
        @ViewBuilder content: () -> V
    ) -> some View where V : View
    

##  Parameters

`alignment`

    

The alignment that the modifier uses to position the implicit `ZStack` that
groups the background views. The default is `center`.

`container`

    

The container that will use the background.

`content`

    

The view to use as the background of the container.

## Discussion

The following example uses a custom `View` as a background:

The `.containerBackground(for:alignment:content:)` modifier differs from the
`background(_:ignoresSafeAreaEdges:)` modifier by automatically filling an
entire parent container. `ContainerBackgroundPlacement` describes the
available containers.

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`struct ContainerBackgroundPlacement`

The placement of a container background.

Structure

# ContainerBackgroundPlacement

The placement of a container background.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    struct ContainerBackgroundPlacement

## Overview

This method controls where to place a background that you specify with the
`containerBackground(_:for:)` or `containerBackground(for:alignment:content:)`
modifier.

## Topics

### Getting placements

`static let navigation: ContainerBackgroundPlacement`

A background placement inside a `NavigationStack` or `NavigationSplitView`

`static let tabView: ContainerBackgroundPlacement`

A background placement inside a `TabView`.

`static let widget: ContainerBackgroundPlacement`

The container background placement for a widget.

### Getting StoreKit placements

`static var subscriptionStore: ContainerBackgroundPlacement`

A background placement inside a `SubscriptionStoreView`.

`static var subscriptionStoreFullHeight: ContainerBackgroundPlacement`

A background placement that spans the full height of a
`SubscriptionStoreView`.

`static var subscriptionStoreHeader: ContainerBackgroundPlacement`

A background placement inside the marketing content of a
`SubscriptionStoreView`

## Relationships

### Conforms To

  * `Equatable`
  * `Hashable`
  * `Sendable`

## See Also

### Layering views

Adding a background to your view

Compose a background behind your view and extend it beyond the safe area
insets.

`struct ZStack`

A view that overlays its subviews, aligning them in both axes.

`func zIndex(Double) -> some View`

Controls the display order of overlapping views.

`func background<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify behind this view.

`func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to a style.

`func background(ignoresSafeAreaEdges: Edge.Set) -> some View`

Sets the view’s background to the default background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to an insettable shape filled with the default
background style.

`func background<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with a style.

`func background<S>(in: S, fillStyle: FillStyle) -> some View`

Sets the view’s background to a shape filled with the default background
style.

`func overlay<V>(alignment: Alignment, content: () -> V) -> some View`

Layers the views that you specify in front of this view.

`func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View`

Layers the specified style in front of this view.

`func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View`

Layers a shape that you specify in front of this view.

`var backgroundMaterial: Material?`

The material underneath the current view.

`func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some
View`

Sets the container background of the enclosing container using a view.

`func containerBackground<V>(for: ContainerBackgroundPlacement, alignment:
Alignment, content: () -> V) -> some View`

Sets the container background of the enclosing container using a view.

Structure

# ViewThatFits

A view that adapts to the available space by providing the first child view
that fits.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  tvOS 16.0+  watchOS
9.0+  visionOS 1.0+

    
    
    @frozen
    struct ViewThatFits<Content> where Content : View

## Overview

`ViewThatFits` evaluates its child views in the order you provide them to the
initializer. It selects the first child whose ideal size on the constrained
axes fits within the proposed size. This means that you provide views in order
of preference. Usually this order is largest to smallest, but since a view
might fit along one constrained axis but not the other, this isn’t always the
case. By default, `ViewThatFits` constrains in both the horizontal and
vertical axes.

The following example shows an `UploadProgressView` that uses `ViewThatFits`
to display the upload progress in one of three ways. In order, it attempts to
display:

  * An `HStack` that contains a `Text` view and a `ProgressView`.

  * Only the `ProgressView`.

  * Only the `Text` view.

The progress views are fixed to a 100-point width.

This use of `ViewThatFits` evaluates sizes only on the horizontal axis. The
following code fits the `UploadProgressView` to several fixed widths:

## Topics

### Creating a view that fits

`init(in: Axis.Set, content: () -> Content)`

Produces a view constrained in the given axes from one of several alternatives
provided by a view builder.

## Relationships

### Conforms To

  * `View`

Structure

# Spacer

A flexible space that expands along the major axis of its containing stack
layout, or on both axes if not contained in a stack.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    @frozen
    struct Spacer

## Overview

A spacer creates an adaptive view with no content that expands as much as it
can. For example, when placed within an `HStack`, a spacer expands
horizontally as much as the stack allows, moving sibling views out of the way,
within the limits of the stack’s size. SwiftUI sizes a stack that doesn’t
contain a spacer up to the combined ideal widths of the content of the stack’s
child views.

The following example provides a simple checklist row to illustrate how you
can use a spacer:

Adding a spacer before the image creates an adaptive view with no content that
expands to push the image and text to the right side of the stack. The stack
also now expands to take as much space as the parent view allows, shown by the
blue border that indicates the boundary of the stack:

Moving the spacer between the image and the name pushes those elements to the
left and right sides of the `HStack`, respectively. Because the stack contains
the spacer, it expands to take as much horizontal space as the parent view
allows; the blue border indicates its size:

Adding two spacer views on the outside of the stack leaves the image and text
together, while the stack expands to take as much horizontal space as the
parent view allows:

## Topics

### Creating a spacer

`init(minLength: CGFloat?)`

`var minLength: CGFloat?`

The minimum length this spacer can be shrunk to, along the axis or axes of
expansion.

## Relationships

### Conforms To

  * `Sendable`
  * `View`

## See Also

### Separators

`struct Divider`

A visual element that can be used to separate other content.

Structure

# Divider

A visual element that can be used to separate other content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    struct Divider

## Overview

When contained in a stack, the divider extends across the minor axis of the
stack, or horizontally when not in a stack.

## Topics

### Creating a divider

`init()`

## Relationships

### Conforms To

  * `View`

## See Also

### Separators

`struct Spacer`

A flexible space that expands along the major axis of its containing stack
layout, or on both axes if not contained in a stack.




Protocol

# AccessibilityRotorContent

Content within an accessibility rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    protocol AccessibilityRotorContent

## Overview

Generally generated from control flow constructs like `ForEach` and `if`, and
`AccessibilityRotorEntry`.

## Topics

### Supporting types

`var body: Self.Body`

The internal content of this `AccessibilityRotorContent`.

**Required**

` associatedtype Body : AccessibilityRotorContent`

The type for the internal content of this `AccessibilityRotorContent`.

**Required**

## Relationships

### Conforming Types

  * `AccessibilityRotorEntry`

Conforms when `ID` conforms to `Hashable`.

  * `ForEach`

Conforms when `Data` conforms to `RandomAccessCollection`, `ID` conforms to
`Hashable`, and `Content` conforms to `AccessibilityRotorContent`.

  * `Group`

Conforms when `Content` conforms to `AccessibilityRotorContent`.

## See Also

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`struct AccessibilityRotorContentBuilder`

Result builder you use to generate rotor entry content.

`struct AccessibilityRotorEntry`

A struct representing an entry in an Accessibility Rotor.

Available when `ID` conforms to `Hashable`.

Structure

# AccessibilityRotorContentBuilder

Result builder you use to generate rotor entry content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    @resultBuilder
    struct AccessibilityRotorContentBuilder

## Topics

### Building navigation content

`static func buildBlock<Content>(Content) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1>(C0, C1) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some
AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) ->
some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5,
C6) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4,
C5, C6, C7) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3,
C4, C5, C6, C7, C8) -> some AccessibilityRotorContent`

`static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2,
C3, C4, C5, C6, C7, C8, C9) -> some AccessibilityRotorContent`

`static func buildIf<Content>(Content?) -> some AccessibilityRotorContent`

`static func buildExpression<Content>(Content) -> Content`

Builds an expression within the builder.

## See Also

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`protocol AccessibilityRotorContent`

Content within an accessibility rotor.

`struct AccessibilityRotorEntry`

A struct representing an entry in an Accessibility Rotor.

Structure

# AccessibilityRotorEntry

A struct representing an entry in an Accessibility Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilityRotorEntry<ID> where ID : Hashable

## Overview

An Accessibility Rotor is a shortcut for Accessibility users to quickly
navigate to specific elements of the user interface, and optionally specific
ranges of text within those elements.

An entry in a Rotor may contain a label to identify the entry to the user, and
identifier used to determine which Accessibility element the Rotor entry
should navigate to, as well as an optional range used for entries that
navigate to a specific position in the text of their associated Accessibility
element. An entry can also specify a handler to be called before the entry is
navigated to, to do any manual work needed to bring the Accessibility element
on-screen.

In the following example, a Message application creates a Rotor allowing users
to navigate to specifically the messages originating from VIPs.

An entry may also be created using an optional namespace, for situations where
there are multiple Accessibility elements within a ForEach iteration or where
a `ScrollView` is not present. In this case, the `prepare` closure may be
needed in order to scroll the element into position using `ScrollViewReader`.
The same namespace should be passed to calls to
`accessibilityRotorEntry(id:in:)` to tag the Accessibility elements associated
with this entry.

In the following example, a Message application creates a Rotor allowing users
to navigate to specifically the messages originating from VIPs. The Rotor
entries are associated with the content text of the message, which is one of
the two views within the ForEach that generate Accessibility elements. That
view is tagged with `accessibilityRotorEntry(id:in:)` so that it can be found
by the `AccessibilityRotorEntry`, and `ScrollViewReader` is used with the
`prepare` closure to scroll it into position.

## Topics

### Creating a rotor entry

`init(LocalizedStringKey, textRange: Range<String.Index>, prepare: (() ->
Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init<L>(L, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init(Text?, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

### Creating a rotor entry with an identifier

`init(LocalizedStringKey, id: ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init<L>(L, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init(Text, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

### Creating an identified rotor entry in a namespace

`init(LocalizedStringKey, id: ID, in: Namespace.ID, textRange:
Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init(Text, id: ID, in: Namespace.ID, textRange: Range<String.Index>?,
prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

## Relationships

### Conforms To

  * `AccessibilityRotorContent`

Conforms when `ID` conforms to `Hashable`.

## See Also

### Creating rotors

`func accessibilityRotor<Content>(LocalizedStringKey, entries: () -> Content)
-> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<Content>(Text, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`func accessibilityRotor<L, Content>(L, entries: () -> Content) -> some View`

Create an Accessibility Rotor with the specified user-visible label, and
entries generated from the content closure.

`protocol AccessibilityRotorContent`

Content within an accessibility rotor.

Available when `ID` conforms to `Hashable`.

`struct AccessibilityRotorContentBuilder`

Result builder you use to generate rotor entry content.

Structure

# AccessibilitySystemRotor

Designates a Rotor that replaces one of the automatic, system-provided Rotors
with a developer-provided Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    struct AccessibilitySystemRotor

## Topics

### Iterating through text

`static var textFields: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all text fields.

`static var boldText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of bolded text.

`static var italicText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of italicized
text.

`static var underlineText: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of underlined
text.

`static var misspelledWords: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all the ranges of mis-spelled
words.

### Iterating through headings

`static var headings: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all headings.

`static func headings(level: AccessibilityHeadingLevel) ->
AccessibilitySystemRotor`

System Rotors allowing users to iterate through all headings, of various
heading levels.

### Iterating through links

`static var links: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all links.

`static func links(visited: Bool) -> AccessibilitySystemRotor`

System Rotors allowing users to iterate through links or visited links.

### Iterating through other elements

`static var images: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all images.

`static var landmarks: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all landmarks.

`static var lists: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all lists.

`static var tables: AccessibilitySystemRotor`

System Rotor allowing users to iterate through all tables.

## Relationships

### Conforms To

  * `Sendable`

## See Also

### Replacing system rotors

`func accessibilityRotor<Content>(AccessibilitySystemRotor, entries: () ->
Content) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel, ID>(AccessibilitySystemRotor, entries:
[EntryModel], entryID: KeyPath<EntryModel, ID>, entryLabel:
KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor<EntryModel>(AccessibilitySystemRotor, entries:
[EntryModel], entryLabel: KeyPath<EntryModel, String>) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.

`func accessibilityRotor(AccessibilitySystemRotor, textRanges:
[Range<String.Index>]) -> some View`

Create an Accessibility Rotor replacing the specified system-provided Rotor.
The Rotor will be attached to the current Accessibility element, and each
entry will go the specified range of that element.


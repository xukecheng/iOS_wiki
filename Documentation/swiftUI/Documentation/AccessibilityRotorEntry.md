Initializer

# init(_:textRange:prepare:)

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        textRange: Range<String.Index>,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`labelKey`

    

Localized string used to show this Rotor entry to users. If no label is
specified, the Rotor entry will be labeled based on the text at that range.

`range`

    

Range of text associated with this Rotor entry.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element or text on-screen if it
isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

`init<L>(L, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init(Text?, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

Initializer

# init(_:textRange:prepare:)

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<L>(
        _ label: L,
        textRange: Range<String.Index>,
        prepare: @escaping (() -> Void) = {}
    ) where ID == Never, L : StringProtocol

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users. If no label is
specified, the Rotor entry will be labeled based on the text at that range.

`range`

    

Range of text associated with this Rotor entry.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element or text on-screen if it
isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

`init(LocalizedStringKey, textRange: Range<String.Index>, prepare: (() ->
Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init(Text?, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

Initializer

# init(_:textRange:prepare:)

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text? = nil,
        textRange: Range<String.Index>,
        prepare: @escaping (() -> Void) = {}
    ) where ID == Never

##  Parameters

`label`

    

Optional localized string used to show this Rotor entry to users. If no label
is specified, the Rotor entry will be labeled based on the text at that range.

`range`

    

Range of text associated with this Rotor entry.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element or text on-screen if it
isn’t already, and SwiftUI not able to automatically scroll to it.

## See Also

### Creating a rotor entry

`init(LocalizedStringKey, textRange: Range<String.Index>, prepare: (() ->
Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

`init<L>(L, textRange: Range<String.Index>, prepare: (() -> Void))`

Create a Rotor entry with a specific label and range. This Rotor entry will be
associated with the Accessibility element that owns the Rotor.

Initializer

# init(_:id:textRange:prepare:)

Create a Rotor entry with a specific label and identifier, with an optional
range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        id: ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
should be used within a `scrollView`, either in a `ForEach` or using an `id`
call.

`label`

    

Localized string used to show this Rotor entry to users.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element on-screen if it isn’t
already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry with an identifier

`init<L>(L, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init(Text, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

Initializer

# init(_:id:textRange:prepare:)

Create a Rotor entry with a specific label and identifier, with an optional
range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<L>(
        _ label: L,
        id: ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    ) where L : StringProtocol

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
should be used within a `scrollView`, either in a `ForEach` or using an `id`
call.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element on-screen if it isn’t
already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry with an identifier

`init(LocalizedStringKey, id: ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init(Text, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

Initializer

# init(_:id:textRange:prepare:)

Create a Rotor entry with a specific label and identifier, with an optional
range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text,
        id: ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
should be used within a `scrollView`, either in a `ForEach` or using an `id`
call.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the either label or accessibility value of
the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This can be used to bring the UI element on-screen if it isn’t
already, and SwiftUI is not able to automatically scroll to it.

## See Also

### Creating a rotor entry with an identifier

`init(LocalizedStringKey, id: ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

`init<L>(L, id: ID, textRange: Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label and identifier, with an optional
range.

Initializer

# init(_:id:in:textRange:prepare:)

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ labelKey: LocalizedStringKey,
        id: ID,
        in namespace: Namespace.ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`labelKey`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
and namespace should match a call to `accessibilityRotorEntry(id:in)`.

`namespace`

    

Namespace for this identifier. Should match a call to
`accessibilityRotorEntry(id:in)`.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This should be used to bring the Accessibility element on-
screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

`init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init(Text, id: ID, in: Namespace.ID, textRange: Range<String.Index>?,
prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

Initializer

# init(_:_:in:textRange:prepare:)

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<L>(
        _ label: L,
        _ id: ID,
        in namespace: Namespace.ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    ) where L : StringProtocol

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
and namespace should match a call to `accessibilityRotorEntry(id:in)`.

`namespace`

    

Namespace for this identifier. Should match a call to
`accessibilityRotorEntry(id:in)`.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This should be used to bring the Accessibility element on-
screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

`init(LocalizedStringKey, id: ID, in: Namespace.ID, textRange:
Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init(Text, id: ID, in: Namespace.ID, textRange: Range<String.Index>?,
prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

Initializer

# init(_:id:in:textRange:prepare:)

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ label: Text,
        id: ID,
        in namespace: Namespace.ID,
        textRange: Range<String.Index>? = nil,
        prepare: @escaping (() -> Void) = {}
    )

##  Parameters

`label`

    

Localized string used to show this Rotor entry to users.

`id`

    

Used to find the UI element associated with this Rotor entry. This identifier
and namespace should match a call to `accessibilityRotorEntry(id:in)`.

`namespace`

    

Namespace for this identifier. Should match a call to
`accessibilityRotorEntry(id:in)`.

`textRange`

    

Optional range of text associated with this Rotor entry. This should be a
range within text that is set as the accessibility label or accessibility
value of the associated element.

`prepare`

    

Optional closure to run before a Rotor entry is navigated to, to prepare the
UI as needed. This should be used to bring the Accessibility element on-
screen, if scrolling is needed to get to it.

## See Also

### Creating an identified rotor entry in a namespace

`init(LocalizedStringKey, id: ID, in: Namespace.ID, textRange:
Range<String.Index>?, prepare: (() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.

`init<L>(L, ID, in: Namespace.ID, textRange: Range<String.Index>?, prepare:
(() -> Void))`

Create a Rotor entry with a specific label, identifier and namespace, and with
an optional range.


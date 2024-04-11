Initializer

# init(content:)

Creates a section with the provided section content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V>(@TableRowBuilder<V> content: () -> Content) where Parent == EmptyTableRowContent<V>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

##  Parameters

`content`

    

The section’s content.

## See Also

### Creating a section

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

Initializer

# init(content:)

Creates a section with the provided section content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(@ViewBuilder content: () -> Content)

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

##  Parameters

`content`

    

The section’s content.

## See Also

### Creating a section

`init<V>(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

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

Initializer

# init(_:content:)

Creates a section with the provided section content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        @ViewBuilder content: () -> Content
    )

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

##  Parameters

`titleKey`

    

The key for the section’s localized title, which describes the contents of the
section.

`content`

    

The section’s content.

## See Also

### Creating a section

`init<V>(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init(content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

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

Initializer

# init(_:content:)

Creates a section with the provided section content.

iOS 15.0+  iPadOS 15.0+  macOS 12.0+  Mac Catalyst 15.0+  tvOS 15.0+  watchOS
8.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

##  Parameters

`title`

    

A string that describes the contents of the section.

`content`

    

The section’s content.

## See Also

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

`init<V, S>(S, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init<V>(LocalizedStringKey, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

Initializer

# init(_:content:)

Creates a section with the provided section content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V, S>(
        _ title: S,
        @TableRowBuilder<V> content: () -> Content
    ) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, S : StringProtocol

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

##  Parameters

`title`

    

A string that describes the contents of the section.

`content`

    

The section’s content.

## See Also

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

`init<V>(LocalizedStringKey, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

Initializer

# init(_:content:)

Creates a section with the provided section content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        @TableRowBuilder<V> content: () -> Content
    ) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

##  Parameters

`titleKey`

    

The key for the section’s localized title, which describes the contents of the
section.

`content`

    

The section’s content.

## See Also

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

Initializer

# init(content:header:)

Creates a section with a header and the provided section content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder header: () -> Parent
    )

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

##  Parameters

`content`

    

The section’s content.

`header`

    

A view to use as the section’s header.

## See Also

### Adding headers and footers

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

Initializer

# init(content:header:)

Creates a section with a header and the provided section content.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    init<V, H>(
        @TableRowBuilder<V> content: () -> Content,
        @ViewBuilder header: () -> H
    ) where Parent == TableHeaderRowContent<V, H>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, H : View

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

##  Parameters

`content`

    

The section’s content.

`header`

    

A view to use as the section’s header.

## See Also

### Adding headers and footers

`init(content: () -> Content, header: () -> Parent)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init(content: () -> Content, footer: () -> Footer)`

Creates a section with a footer and the provided section content.

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

`init(content: () -> Content, header: () -> Parent, footer: () -> Footer)`

Creates a section with a header, footer, and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Initializer

# init(content:footer:)

Creates a section with a footer and the provided section content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder footer: () -> Footer
    )

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

##  Parameters

`content`

    

The section’s content.

`footer`

    

A view to use as the section’s footer.

## See Also

### Adding headers and footers

`init(content: () -> Content, header: () -> Parent)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

`init<V, H>(content: () -> Content, header: () -> H)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to
`TableRowContent`, and `Footer` conforms to `TableRowContent`.

`init(content: () -> Content, header: () -> Parent, footer: () -> Footer)`

Creates a section with a header, footer, and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Initializer

# init(content:header:footer:)

Creates a section with a header, footer, and the provided section content.

iOS 13.0+  iPadOS 13.0+  macOS 10.15+  Mac Catalyst 13.0+  tvOS 13.0+  watchOS
6.0+  visionOS 1.0+

    
    
    init(
        @ViewBuilder content: () -> Content,
        @ViewBuilder header: () -> Parent,
        @ViewBuilder footer: () -> Footer
    )

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

##  Parameters

`content`

    

The section’s content.

`header`

    

A view to use as the section’s header.

`footer`

    

A view to use as the section’s footer.

## See Also

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

Initializer

# init(_:isExpanded:content:)

Creates a section with the provided section content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<V, S>(
        _ title: S,
        isExpanded: Binding<Bool>,
        @TableRowBuilder<V> content: () -> Content
    ) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, S : StringProtocol

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

##  Parameters

`title`

    

A string that describes the contents of the section.

`isExpanded`

    

A binding to a Boolean value that determines the section’s expansion state
(expanded or collapsed).

`content`

    

The section’s content.

## See Also

### Controlling collapsibility

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

Initializer

# init(_:isExpanded:content:)

Creates a section with the provided section content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init<S>(
        _ title: S,
        isExpanded: Binding<Bool>,
        @ViewBuilder content: () -> Content
    ) where S : StringProtocol

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

##  Parameters

`title`

    

A string that describes the contents of the section.

`isExpanded`

    

A binding to a Boolean value that determines the section’s expansion state
(expanded or collapsed).

`content`

    

The section’s content.

## See Also

### Controlling collapsibility

`init<V, S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

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

Initializer

# init(_:isExpanded:content:)

Creates a section with the provided section content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<V>(
        _ titleKey: LocalizedStringKey,
        isExpanded: Binding<Bool>,
        @TableRowBuilder<V> content: () -> Content
    ) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

##  Parameters

`titleKey`

    

The key for the section’s localized title, which describes the contents of the
section.

`isExpanded`

    

A binding to a Boolean value that determines the section’s expansion state
(expanded or collapsed).

`content`

    

The section’s content.

## See Also

### Controlling collapsibility

`init<V, S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

`init<S>(S, isExpanded: Binding<Bool>, content: () -> Content)`

Creates a section with the provided section content.

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

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

Initializer

# init(_:isExpanded:content:)

Creates a section with the provided section content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        _ titleKey: LocalizedStringKey,
        isExpanded: Binding<Bool>,
        @ViewBuilder content: () -> Content
    )

Available when `Parent` is `Text`, `Content` conforms to `View`, and `Footer`
is `EmptyView`.

##  Parameters

`titleKey`

    

The key for the section’s localized title, which describes the contents of the
section.

`isExpanded`

    

A binding to a Boolean value that determines the section’s expansion state
(expanded or collapsed).

`content`

    

The section’s content.

## See Also

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

Initializer

# init(isExpanded:content:header:)

Creates a section with a header, the provided section content, and a binding
representing the section’s expansion state.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  tvOS 17.0+  watchOS
10.0+  visionOS 1.0+

    
    
    init(
        isExpanded: Binding<Bool>,
        @ViewBuilder content: () -> Content,
        @ViewBuilder header: () -> Parent
    )

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

##  Parameters

`isExpanded`

    

A binding to a Boolean value that determines the section’s expansion state
(expanded or collapsed).

`content`

    

The section’s content.

`header`

    

A view to use as the section’s header.

## See Also

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

`init<V, H>(isExpanded: Binding<Bool>, content: () -> Content, header: () ->
H)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

Initializer

# init(isExpanded:content:header:)

Creates a section with a header and the provided section content.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    init<V, H>(
        isExpanded: Binding<Bool>,
        @TableRowBuilder<V> content: () -> Content,
        @ViewBuilder header: () -> H
    ) where Parent == TableHeaderRowContent<V, H>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, H : View

Available when `Parent` conforms to `TableRowContent` and `Content` conforms
to `TableRowContent`.

##  Parameters

`isExpanded`

    

A binding to a Boolean value that determines the section’s expansion state
(expanded or collapsed).

`content`

    

The section’s content.

`header`

    

A view to use as the section’s header.

## See Also

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

Initializer

# init(header:content:)

Creates a section with a header and the provided section content.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        header: Parent,
        @ViewBuilder content: () -> Content
    )

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

Deprecated

Use `init(content:header:)` instead.

##  Parameters

`header`

    

A view to use as the section’s header.

`content`

    

The section’s content.

## See Also

### Deprecated symbols

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

Initializer

# init(footer:content:)

Creates a section with a footer and the provided section content.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        footer: Footer,
        @ViewBuilder content: () -> Content
    )

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

Use `init(content:footer:)` instead.

##  Parameters

`footer`

    

A view to use as the section’s footer.

`content`

    

The section’s content.

## See Also

### Deprecated symbols

`init(header: Parent, content: () -> Content)`

Creates a section with a header and the provided section content.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` is `EmptyView`.

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

Initializer

# init(header:footer:content:)

Creates a section with a header, footer, and the provided section content.

iOS 13.0–17.4  Deprecated  iPadOS 13.0–17.4  Deprecated  macOS 10.15–14.4
Deprecated  Mac Catalyst 13.0–17.4  Deprecated  tvOS 13.0–17.4  Deprecated
watchOS 6.0–10.4  Deprecated  visionOS 1.0+

    
    
    init(
        header: Parent,
        footer: Footer,
        @ViewBuilder content: () -> Content
    )

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

Use `init(content:header:footer:)` instead.

##  Parameters

`header`

    

A view to use as the section’s header.

`footer`

    

A view to use as the section’s footer.

`content`

    

The section’s content.

## See Also

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

`func collapsible(Bool) -> some View`

Sets whether a section can be collapsed by the user.

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

Instance Method

# collapsible(_:)

Sets whether a section can be collapsed by the user.

macOS 10.15–14.4  Deprecated

    
    
    func collapsible(_ collapsible: Bool) -> some View
    

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and
`Footer` conforms to `View`.

Deprecated

To disable collapsibility in macOS 14 and later, use one of the `Section`
initializers that lacks collapsibility.

## Discussion

This modifier only applies to sections in `List` views that have the `sidebar`
style.

## See Also

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


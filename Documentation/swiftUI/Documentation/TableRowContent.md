Instance Property

# tableRowBody

The composition of content that comprise the table row content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    var tableRowBody: Self.TableRowBody { get }

**Required**

## See Also

### Getting the row body

`associatedtype TableRowBody : TableRowContent`

The type of content representing the body of this table row content.

**Required**

Associated Type

# TableRowBody

The type of content representing the body of this table row content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype TableRowBody : TableRowContent

**Required**

## See Also

### Getting the row body

`var tableRowBody: Self.TableRowBody`

The composition of content that comprise the table row content.

**Required**

Associated Type

# TableRowValue

The type of value represented by this table row content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    associatedtype TableRowValue : Identifiable = Self.TableRowBody.TableRowValue

**Required**

Instance Method

# draggable(_:)

Activates this row as the source of a drag and drop operation.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some TableRowContent<Self.TableRowValue> where T : Transferable
    

##  Parameters

`payload`

    

A closure that returns a single instance or a value conforming to
`Transferable` that represents the draggable data from this view.

## Return Value

A row that activates this row as the source of a drag and drop operation.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag
and drop to this row.

## See Also

### Managing interaction

`func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Defines the entire row as a destination of a drag and drop operation that
handles the dropped content with a closure that you specify.

`func onHover(perform: (Bool) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Adds an action to perform when the pointer moves onto or away from the entire
row.

`func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self,
ItemProviderTableRowModifier>`

Provides a closure that vends the drag representation for a particular data
element.

`struct ItemProviderTableRowModifier`

A table row modifier that associates an item provider with some base row
content.

Instance Method

# dropDestination(for:action:)

Defines the entire row as a destination of a drag and drop operation that
handles the dropped content with a closure that you specify.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func dropDestination<T>(
        for payloadType: T.Type = T.self,
        action: @escaping ([T]) -> Void
    ) -> some TableRowContent<Self.TableRowValue> where T : Transferable
    

##  Parameters

`payloadType`

    

The expected type of the dropped models.

`action`

    

A closure that takes the dropped content and responds with `true` if the drop
operation was successful; otherwise, return `false`.

## Return Value

A row that provides a drop destination for a drag operation of the specified
type.

## See Also

### Managing interaction

`func draggable<T>(() -> T) -> some TableRowContent<Self.TableRowValue> `

Activates this row as the source of a drag and drop operation.

`func onHover(perform: (Bool) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Adds an action to perform when the pointer moves onto or away from the entire
row.

`func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self,
ItemProviderTableRowModifier>`

Provides a closure that vends the drag representation for a particular data
element.

`struct ItemProviderTableRowModifier`

A table row modifier that associates an item provider with some base row
content.

Instance Method

# onHover(perform:)

Adds an action to perform when the pointer moves onto or away from the entire
row.

macOS 14.0+  visionOS 1.0+

    
    
    func onHover(perform action: @escaping (Bool) -> Void) -> some TableRowContent<Self.TableRowValue>
    

## See Also

### Managing interaction

`func draggable<T>(() -> T) -> some TableRowContent<Self.TableRowValue> `

Activates this row as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Defines the entire row as a destination of a drag and drop operation that
handles the dropped content with a closure that you specify.

`func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self,
ItemProviderTableRowModifier>`

Provides a closure that vends the drag representation for a particular data
element.

`struct ItemProviderTableRowModifier`

A table row modifier that associates an item provider with some base row
content.

Instance Method

# itemProvider(_:)

Provides a closure that vends the drag representation for a particular data
element.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func itemProvider(_ action: (() -> NSItemProvider?)?) -> ModifiedContent<Self, ItemProviderTableRowModifier>

## See Also

### Managing interaction

`func draggable<T>(() -> T) -> some TableRowContent<Self.TableRowValue> `

Activates this row as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Defines the entire row as a destination of a drag and drop operation that
handles the dropped content with a closure that you specify.

`func onHover(perform: (Bool) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Adds an action to perform when the pointer moves onto or away from the entire
row.

`struct ItemProviderTableRowModifier`

A table row modifier that associates an item provider with some base row
content.

Structure

# ItemProviderTableRowModifier

A table row modifier that associates an item provider with some base row
content.

iOS 16.0+  iPadOS 16.0+  macOS 12.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    struct ItemProviderTableRowModifier

## See Also

### Managing interaction

`func draggable<T>(() -> T) -> some TableRowContent<Self.TableRowValue> `

Activates this row as the source of a drag and drop operation.

`func dropDestination<T>(for: T.Type, action: ([T]) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Defines the entire row as a destination of a drag and drop operation that
handles the dropped content with a closure that you specify.

`func onHover(perform: (Bool) -> Void) -> some
TableRowContent<Self.TableRowValue> `

Adds an action to perform when the pointer moves onto or away from the entire
row.

`func itemProvider((() -> NSItemProvider?)?) -> ModifiedContent<Self,
ItemProviderTableRowModifier>`

Provides a closure that vends the drag representation for a particular data
element.

Instance Method

# contextMenu(menuItems:)

Adds a context menu to a table row.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func contextMenu<M>(@ViewBuilder menuItems: () -> M) -> ModifiedContent<Self, _ContextMenuTableRowModifier<M>> where M : View

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

## Return Value

A row that can display a context menu.

## Discussion

Use this modifier to add a context menu to a table row. Compose the menu by
returning controls like `Button`, `Toggle`, and `Picker` from the `menuItems`
closure. You can also use `Menu` to define submenus, or `Section` to group
items.

The following example adds a context menu to each row in a table that people
can use to send an email to the person represented by that row:

If you want to display a preview beside the context menu, use
`contextMenu(menuItems:preview:)`. If you want to display a context menu
that’s based on the current selection, use
`contextMenu(forSelectionType:menu:primaryAction:)`. To add context menus to
other kinds of views, use `contextMenu(menuItems:)`.

## See Also

### Adding a context menu to a row

`func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) ->
ModifiedContent<Self, _ContextMenuPreviewTableRowModifier<M, P>>`

Adds a context menu with a preview to a table row.

Instance Method

# contextMenu(menuItems:preview:)

Adds a context menu with a preview to a table row.

iOS 16.0+  iPadOS 16.0+  macOS 13.0+  Mac Catalyst 16.0+  visionOS 1.0+

    
    
    func contextMenu<M, P>(
        @ViewBuilder menuItems: () -> M,
        @ViewBuilder preview: () -> P
    ) -> ModifiedContent<Self, _ContextMenuPreviewTableRowModifier<M, P>> where M : View, P : View

##  Parameters

`menuItems`

    

A closure that produces the menu’s contents. You can deactivate the context
menu by returning nothing from the closure.

`preview`

    

A view that the system displays along with the menu.

## Return Value

A row that can display a context menu with a preview.

## Discussion

When you use this modifier to add a context menu to rows in a table, the
system shows a preview beside the menu. Compose the menu by returning controls
like `Button`, `Toggle`, and `Picker` from the `menuItems` closure. You can
also use `Menu` to define submenus.

Define the preview by returning a view from the `preview` closure. The system
sizes the preview to match the size of its content. For example, the following
code adds a context menu with a preview to each row in a table that people can
use to send an email to the person represented by that row:

Note

This view modifier produces a context menu on macOS, but that platform doesn’t
display the preview.

If you don’t need a preview, use `contextMenu(menuItems:)`. If you want to
display a context menu that’s based on the current selection, use
`contextMenu(forSelectionType:menu:primaryAction:)`. To add context menus to
other kinds of views, see `contextMenu(menuItems:)`.

## See Also

### Adding a context menu to a row

`func contextMenu<M>(menuItems: () -> M) -> ModifiedContent<Self,
_ContextMenuTableRowModifier<M>>`

Adds a context menu to a table row.

Instance Method

# selectionDisabled(_:)

Adds a condition that controls whether users can select this row.

iOS 17.0+  iPadOS 17.0+  macOS 14.0+  Mac Catalyst 17.0+  visionOS 1.0+

    
    
    func selectionDisabled(_ isDisabled: Bool = true) -> some TableRowContent<Self.TableRowValue>
    

##  Parameters

`isDisabled`

    

A Boolean value that determines whether users can select this row.

## Discussion

Use this modifier to control the selectability of views in selectable
containers like `List` or `Table`. In the example, below, the user can’t
select the first item in the table.

You can also use this modifier to specify the selectability of views within a
`Picker`. The following example represents a flavor picker that disables
selection on flavors that are unavailable.


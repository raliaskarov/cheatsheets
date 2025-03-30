# Common CSS styles 

## Position

Specifies the type of positioning method used for an element.
    Positioning determines how an element is placed within its containing block and how it interacts with other elements.

    Example: position: relative;
        This sets the element's position relative to its normal position.
    Values:
        static: The default positioning.
        relative: Positioned relative to its normal position.
        absolute: Positioned relative to the nearest positioned ancestor.
        fixed: Positioned relative to the browser window.
        sticky: Switches between relative and fixed based on the scroll position.
        Default value: static

- static: This is the default positioning. The element appears in the normal flow of the page, and properties like top, left, right, and bottom have no effect.
- relative: The element is still in the normal flow, but you can offset it relative to its normal position using properties like top, left, etc. For example, if you add left: 20px; to your <p>, it will shift 20 pixels to the right from where it would normally be.
- absolute: The element is removed from the normal flow and positioned relative to its nearest positioned ancestor (an ancestor with a position value other than static), or the document body if none exists.
- fixed: The element is removed from the normal flow and positioned relative to the viewport, meaning it stays in the same place even when scrolling.
- sticky: This is a hybrid of relative and fixed positioning. The element acts like a relatively positioned element until it reaches a certain point on the page, then it becomes fixed.

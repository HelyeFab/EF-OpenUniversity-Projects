public class Tree {
    private Square trunk;
    private Triangle leaves;
    private boolean isVisible;

    /**
     * Create a new tree at default position with default color.
     */
    public Tree() {
        // Create the trunk (red square)
        trunk = new Square();
        trunk.changeColor("brown");
        trunk.changeSize(60); // Default square size is 60x60
        trunk.moveHorizontal(310 - 310); // No horizontal movement needed (trunk's default is at 310)
        trunk.moveVertical(120 - 120); // No vertical movement needed (trunk's default is at 120)

        // Create the leaves (green triangle)
        leaves = new Triangle();
        leaves.changeColor("green");
        leaves.changeSize(90, 120); // 

        // Adjust the leaves to the exact position (210, 140)
        leaves.moveHorizontal(210 - 80); // Move horizontally to (210)
        leaves.moveVertical(30 - 120); // Move vertically to (140)
        isVisible = false;
    }

    /**
     * Make this tree visible. If it was already visible, do nothing.
     */
    public void makeVisible() {
        if (!isVisible) {
            trunk.makeVisible();
            leaves.makeVisible();
            isVisible = true;
        }
    }

    /**
     * Make this tree invisible. If it was already invisible, do nothing.
     */
    public void makeInvisible() {
        if (isVisible) {
            trunk.makeInvisible();
            leaves.makeInvisible();
            isVisible = false;
        }
    }

    /**
     * Move the tree to a new horizontal and vertical position.
     */
    public void moveHorizontal(int distance) {
        trunk.moveHorizontal(distance);
        leaves.moveHorizontal(distance);
    }

    public void moveVertical(int distance) {
        trunk.moveVertical(distance);
        leaves.moveVertical(distance);
    }

    /**
     * Change the color of the tree.
     * 
     * @param trunkColor  The color for the trunk.
     * @param leavesColor The color for the leaves.
     */
    public void changeColor(String trunkColor, String leavesColor) {
        trunk.changeColor(trunkColor);
        leaves.changeColor(leavesColor);
    }

    /**
     * Change the size of the tree by setting a new trunk size and leaves size.
     * 
     * @param trunkSize    The size of the trunk.
     * @param leavesWidth  The width of the leaves.
     * @param leavesHeight The height of the leaves.
     */
    public void changeSize(int trunkSize, int leavesWidth, int leavesHeight) {
        trunk.changeSize(trunkSize);
        leaves.changeSize(leavesWidth, leavesHeight);
    }
}

#include <iostream>
#include <GL/glut.h>
#include <cmath>

using namespace std;

void putpixel(int x, int y) {
    glBegin(GL_POINTS);
    glVertex2i(x, y);
    glEnd();
    glFlush();
}

void DDAlgorithm(int x1, int x2, int y1, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int x = x1;
    int y = y1;
    int step = max(abs(dx), abs(dy));
    float xIncrement = static_cast<float>(dx) / step;
    float yIncrement = static_cast<float>(dy) / step;
    putpixel(round(x), round(y));
    for (int i = 0; i < step; i++) {
        x += xIncrement;
        y += yIncrement;
        putpixel(round(x), round(y));
    }
}

void BHAlgorithm(int x1, int x2, int y1, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;
    int d = 2 * dy - dx;
    int x = x1;
    int y = y1;

    while (x < x2) {
        x++;
        if (d < 0) {
            d += 2 * dy;
        } else {
            y++;
            d += 2 * (dy - dx);
        }
        putpixel(x, y);
    }
}

void midPointCircleDrawing(int xCenter, int yCenter, int radius) {
    int x = 0;
    int y = radius;
    int p = 1 - radius;
    while (x < y) {
        putpixel(xCenter + x, yCenter - y);
        putpixel(xCenter + x, yCenter + y);
        putpixel(xCenter - x, yCenter + y);
        putpixel(xCenter - x, yCenter - y);
        putpixel(xCenter +y, yCenter +x);
        putpixel(xCenter +y, yCenter -x);
        putpixel(xCenter -y, yCenter +x);
        putpixel(xCenter -y, yCenter -x);
        x++;
        if (p < 0) {
            p += 2 * x + 1;
        } else {
            y--;
            p += 2 * (x - y) + 1;
        }
    }
}

void reshape(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, width, 0, height);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutCreateWindow("OpenGL Line and Circle Drawing");

    glutReshapeFunc(reshape);
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0, 0.0, 0.0);

    bool running = true;
    int choice;
    int lineChoice;

    while (running) {
        cout << "Line and Circle Drawing program!" << endl;
        cout << "To draw line, enter 1!" << endl;
        cout << "To draw circle, enter 2" << endl;
        cout << "To quit the program, enter any other number" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            do {
                cout << "Choose line drawing algorithm:" << endl;
                cout << "For DDA algorithm, enter 1" << endl;
                cout << "For BHA Algorithm, enter 2" << endl;
                cin >> lineChoice;
            } while (lineChoice != 1 && lineChoice != 2);

            int x1, x2, y1, y2;
            cout << "Enter x1: ";
            cin >> x1;
            cout << "Enter x2: ";
            cin >> x2;
            cout << "Enter y1: ";
            cin >> y1;
            cout << "Enter y2: ";
            cin >> y2;

            switch (lineChoice) {
                case 1:
                    DDAlgorithm(x1, x2, y1, y2);
                    break;
                case 2:
                    int dx = x2 - x1;
                    int dy = y2 - y1;
                    float slope = static_cast<float>(dy) / dx;
                    if (slope < 1 || slope > -1) {
                        BHAlgorithm(x1, x2, y1, y2);
                    } else {
                        BHAlgorithm(y1, y2, x1, x2);
                    }
                    break;
            }
        } else if (choice == 2) {
            do {
                cout << "Choose circle drawing algorithm:" << endl;
                cout << "For mid-point algorithm, enter 1" << endl;
                cin >> lineChoice;
            } while (lineChoice != 1);

            int x, y, radius;
            cout << "Enter xCenter: ";
            cin >> x;
            cout << "Enter yCenter: ";
            cin >> y;
            cout << "Enter Radius: ";
            cin >> radius;

            midPointCircleDrawing(x, y, radius);
        } else {
            running = false;
            break;
        }
    }

    glutMainLoop();

    return 0;
}


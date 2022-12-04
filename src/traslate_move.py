
class TraslateMove:
    
    def traslate_to_minimax(col, row):
        col_traslated: str
        row_traslated: int 
        match col:
            case 0:
                col_traslated = 'a'
            case 1:
                col_traslated = 'b'
            case 2:
                col_traslated = 'c'
            case 3:
                col_traslated = 'd'
            case 4:
                col_traslated = 'e'
            case 5:
                col_traslated = 'f'
            case 6:
                col_traslated = 'g'
            case 7:
                col_traslated = 'h'

        match row:
            case 0:
                row_traslated = '8'
            case 1:
                row_traslated = '7'
            case 2:
                row_traslated = '6'
            case 3:
                row_traslated = '5'
            case 4:
                row_traslated = '4'
            case 5:
                row_traslated = '3'
            case 6:
                row_traslated = '2'
            case 7:
                row_traslated = '1'

        return f'{col_traslated}{row_traslated}'

    def traslate_to_interface(col, row):
        col_traslated: int
        row_traslated: int
        
        match col:
            case 'a':
                col_traslated = 0
            case 'b':
                col_traslated = 1
            case 'c':
                col_traslated = 2
            case 'd':
                col_traslated = 3
            case 'e':
                col_traslated = 4
            case 'f':
                col_traslated = 5
            case 'g':
                col_traslated = 6
            case 'h':
                col_traslated = 7

        match row:
            case '8':
                row_traslated = 0
            case '7':
                row_traslated = 1
            case '6':
                row_traslated = 2
            case '5':
                row_traslated = 3
            case '4':
                row_traslated = 4
            case '3':
                row_traslated = 5
            case '2':
                row_traslated = 6
            case '1':
                row_traslated = 7

        return (col_traslated,row_traslated)


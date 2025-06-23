#include <stdio.h>
#include <stdlib.h>
#include <string.h>



extern int yyparse(void);
extern void yy_switch_to_buffer(struct yy_buffer_state *);
extern struct yy_buffer_state *yy_scan_string(const char *str);
extern void yy_delete_buffer(struct yy_buffer_state *buffer);
extern void yylex_destroy(void);

int parse_sql(const char* input) {
    struct yy_buffer_state *buffer = yy_scan_string(input);
    int result = yyparse();
    yy_delete_buffer(buffer);
    yylex_destroy();
    return result;
}

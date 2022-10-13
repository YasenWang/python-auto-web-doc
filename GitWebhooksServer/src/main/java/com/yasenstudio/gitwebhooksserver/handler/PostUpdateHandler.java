package com.yasenstudio.gitwebhooksserver.handler;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

@Controller
public class PostUpdateHandler {

    /**
     * Handle Post Update.
     *
     * @return
     */
    @ResponseBody
    @PostMapping("/post-update")
    public ResponseEntity<Object> postUpdate(HttpServletRequest request) {
        String projectName = request.getParameter("p");
        if (projectName == null) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).build();
        }
        try {
            Process proc = Runtime.getRuntime().exec ("./hooks/post-update");

        } catch (IOException e) {
            e.printStackTrace();
            // throw new RuntimeException(e);
        }
        return ResponseEntity.ok().body("OK");
    }
}

from flask import Blueprint, request, jsonify, send_file
import qrcode
import io
import base64
from PIL import Image
from qrcode.constants import ERROR_CORRECT_L

qr_bp = Blueprint('qr', __name__)

@qr_bp.route('/generate', methods=['POST'])
def generate_qr():
    try:
        data = request.get_json()
        url = data.get('url')
        frame = data.get('frame', 'none')
        frame_text = data.get('frame_text', '')
        round_inner = data.get('round_inner', 'no')
        round_outer = data.get('round_outer', 'no')
        
        if not url:
            return jsonify({'error': 'URL é obrigatória'}), 400
        
        # Criar QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=16,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Gerar imagem
        img = qr.make_image(fill_color="black", back_color="white")
        if hasattr(img, 'get_image'):
            img = img.get_image()
        # Agora img é PIL.Image.Image
        if isinstance(img, Image.Image) and img.mode != 'RGB':
            img = img.convert('RGB')
        frame_text_size = data.get('frame_text_size')
        img = add_frame_and_text(img, frame, frame_text, round_inner, round_outer, frame_text_size)
        
        # Converter para base64
        img_buffer = io.BytesIO()
        img.save(img_buffer, 'PNG')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'qr_code': f'data:image/png;base64,{img_base64}',
            'url': url
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def add_frame_and_text(img, frame_type, frame_text=None, round_inner='no', round_outer='no', frame_text_size=None):
    from PIL import ImageDraw, ImageFont
    border_size = 20  # moldura preta
    inner_border = 8  # borda interna branca
    inner_radius = 30  # raio do arredondamento dos cantos internos (brancos)
    # Tamanho do texto
    try:
        font_size = int(frame_text_size) if frame_text_size else 32
        if font_size > 54:
            font_size = 54
    except:
        font_size = 32
    # Tamanho da imagem final (moldura preta)
    if frame_type in ("border", "text"):
        # Calcula dimensões para texto se necessário
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        bbox = font.getbbox(frame_text) if frame_type == "text" and frame_text else (0,0,0,0)
        text_width = int(bbox[2] - bbox[0])
        text_height = int(bbox[3] - bbox[1])
        content_width = img.width + 2*inner_border
        content_height = img.height + 2*inner_border
        if frame_type == "text":
            final_width = max(content_width, text_width) + 2*border_size
            final_height = content_height + text_height + 2*border_size + 40
        else:
            final_width = content_width + 2*border_size
            final_height = content_height + 2*border_size
        # Cria fundo preto (moldura)
        if round_outer == 'yes':
            bg = Image.new("RGBA", (final_width, final_height), (0,0,0,0))
            mask = Image.new("L", (final_width, final_height), 0)
            draw = ImageDraw.Draw(mask)
            outer_radius = 30
            draw.rounded_rectangle([(0, 0), (final_width, final_height)], radius=outer_radius, fill=255)
            bg_draw = ImageDraw.Draw(bg)
            bg_draw.rectangle([(0, 0), (final_width, final_height)], fill=(0,0,0,255))
            bg.putalpha(mask)
        else:
            bg = Image.new("RGBA", (final_width, final_height), (0,0,0,255))
        # Cria retângulo branco com cantos arredondados
        white_box = Image.new("RGBA", (content_width, content_height), (255,255,255,0))
        white_mask = Image.new("L", (content_width, content_height), 0)
        draw_white = ImageDraw.Draw(white_mask)
        if round_inner == 'yes':
            draw_white.rounded_rectangle([(0,0),(content_width,content_height)], radius=inner_radius, fill=255)
        else:
            draw_white.rectangle([(0,0),(content_width,content_height)], fill=255)
        draw_white_box = ImageDraw.Draw(white_box)
        draw_white_box.rectangle([(0,0),(content_width,content_height)], fill=(255,255,255,255))
        white_box.putalpha(white_mask)
        # Cola o retângulo branco centralizado na moldura preta
        white_x = (final_width - content_width)//2
        white_y = border_size if frame_type == "text" else (final_height - content_height)//2
        bg.paste(white_box, (white_x, white_y), white_box)
        # Cola o QR Code quadrado centralizado dentro do retângulo branco
        qr_x = white_x + (content_width - img.width)//2
        qr_y = white_y + (content_height - img.height)//2
        bg.paste(img.convert('RGBA'), (qr_x, qr_y), img.convert('RGBA'))
        # Adiciona texto se necessário
        if frame_type == "text" and frame_text:
            draw = ImageDraw.Draw(bg)
            draw.text(((final_width - text_width)//2, white_y + content_height + 20), frame_text, font=font, fill="white")
        return bg
    return img

@qr_bp.route('/download', methods=['POST'])
def download_qr():
    try:
        data = request.get_json()
        url = data.get('url')
        frame = data.get('frame', 'none')
        frame_text = data.get('frame_text', '')
        file_name = data.get('file_name', '').strip()
        round_inner = data.get('round_inner', 'no')
        round_outer = data.get('round_outer', 'no')
        
        if not url:
            return jsonify({'error': 'URL é obrigatória'}), 400
        
        # Criar QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Gerar imagem
        img = qr.make_image(fill_color="black", back_color="white")
        if hasattr(img, 'get_image'):
            img = img.get_image()
        # Agora img é PIL.Image.Image
        if isinstance(img, Image.Image) and img.mode != 'RGB':
            img = img.convert('RGB')
        frame_text_size = data.get('frame_text_size')
        img = add_frame_and_text(img, frame, frame_text, round_inner, round_outer, frame_text_size)
        
        # Salvar em buffer
        img_buffer = io.BytesIO()
        # Salvar como PNG, que suporta transparência
        img.save(img_buffer, 'PNG')
        img_buffer.seek(0)
        
        return send_file(
            img_buffer,
            mimetype='image/png',
            as_attachment=True,
            download_name=(file_name if file_name else 'qr_code') + '.png'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

